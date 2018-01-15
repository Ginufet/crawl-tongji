# -*- coding: utf-8 -*-
import scrapy
from tjbwc.items import TjbwcItem
from tjbwc_spider import TjbwcSpider


class DownloadsSpider(TjbwcSpider):
    name = 'downloads'
    start_urls = [
        "http://baowei.tongji.edu.cn/3066/list.htm"
    ]

    def parse(self, response):
        for sel in response.xpath("//div[@id='wp_news_w6']/ul/li"):
            downloads_item = TjbwcItem()
            time = sel.xpath("./span/text()").extract()[0]
            title = sel.xpath("./a/text()").extract()[0]
            href = self.base_url + sel.xpath("./a/@href").extract()[0]
            downloads_item['title'] = title
            downloads_item['time'] = time
            if href.endswith(".htm"):
                yield scrapy.Request(href, meta={"item": downloads_item}, callback=self.parse_detail)
            else:
                downloads_item['href'] = href
                yield downloads_item
        next_page_sel = response.xpath("//li[@class='page_nav']/a[@class='next']")
        if next_page_sel:
            next_page_url = next_page_sel.xpath("./@href").extract()[0]
            if next_page_url.endswith(".htm"):
                next_page_url = self.base_url + next_page_url
                yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_detail(self, response):
        downloads_item = response.meta['item']
        sel = response.xpath("//div[@class='wp_articlecontent']/p/a/@href")
        if not sel:
            sel = response.xpath("//div[@class='wp_articlecontent']/a/@href")
        href = self.base_url + sel.extract()[0]
        downloads_item['href'] = href
        return downloads_item