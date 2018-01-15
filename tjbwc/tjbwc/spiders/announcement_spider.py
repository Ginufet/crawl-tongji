# -*- coding: utf-8 -*-
import scrapy
from tjbwc.items import TjbwcItem
from tjbwc_spider import TjbwcSpider


class AnnouncementSpider(TjbwcSpider):
    name = 'announcement'
    start_urls = [
        "http://baowei.tongji.edu.cn/3065/list.htm"
    ]

    def parse(self, response):
        for sel in response.xpath("//div[@id='wp_news_w6']/ul/li"):
            announcement_item = TjbwcItem()
            time = sel.xpath("./span/text()").extract()[0]
            title = sel.xpath("./a/text()").extract()[0].replace(' ', '')
            href = self.base_url + sel.xpath("./a/@href").extract()[0]
            announcement_item['title'] = title
            announcement_item['time'] = time
            announcement_item['href'] = href
            yield announcement_item
        next_page_sel = response.xpath("//li[@class='page_nav']/a[@class='next']")
        if next_page_sel:
            next_page_url = next_page_sel.xpath("./@href").extract()[0]
            if next_page_url.endswith(".htm"):
                next_page_url = self.base_url + next_page_url
                yield scrapy.Request(next_page_url, callback=self.parse)
