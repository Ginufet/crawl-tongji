# -*- coding: utf-8 -*-
import scrapy
import os
from tjcwc.items import AnnouncementItem


class AnnouncementSpider(scrapy.Spider):
    name = 'announcement'
    allowed_domains = ["tongji.edu.cn"]
    base_url = "http://tjcwc.tongji.edu.cn/"
    start_urls = [
        "http://tjcwc.tongji.edu.cn/index.php?classid=9701"
    ]
    newest = True

    def parse(self, response):
        for sel in response.xpath("//div[@class='news_list']/ul/li"):
            announcement_item = AnnouncementItem()
            title = sel.xpath("./a/text()").extract()[0]
            href = self.base_url + sel.xpath("./a/@href").extract()[0]
            time = sel.xpath("./span/text()").extract()[0].replace("[", "").replace("]", "")
            announcement_item["title"] = title
            announcement_item["href"] = href
            announcement_item["time"] = time
            yield announcement_item
        page_sel = response.xpath("//div[@class='pager']")
        if page_sel:
            directions = page_sel.xpath("./a")
            for direction in directions:
                if direction.xpath("./text()").extract()[0] == u"下一页":
                    next_page_url = self.base_url + direction.xpath("./@href").extract()[0]
                    yield scrapy.Request(next_page_url, callback=self.parse)
                    break
