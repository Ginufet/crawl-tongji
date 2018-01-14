# -*- coding: utf-8 -*-
import scrapy
from tjcwc.items import GuideItem


class GuideSpider(scrapy.Spider):
    name = 'guide'
    allowed_domains = ["tongji.edu.cn"]
    base_url = "http://tjcwc.tongji.edu.cn/"
    start_urls = [
        "http://tjcwc.tongji.edu.cn/index.php?classid=9728"
    ]

    def parse(self, response):
        for aspect_url_sel in response.xpath("//li[@class='depth_1']/a/@href"):
            aspect_url = self.base_url + aspect_url_sel.extract()
            if aspect_url == "http://tjcwc.tongji.edu.cn/index.php?classid=9778":
                # FAQ
                continue
            yield scrapy.Request(aspect_url, callback=self.parse_aspect)

    def parse_aspect(self, response):
        for sel in response.xpath("//div[@class='news_list']/ul/li"):
            guide_item = GuideItem()
            title = sel.xpath("./a/text()").extract()[0].replace("\n", "").replace(" ", "")
            href = self.base_url + sel.xpath("./a/@href").extract()[0]
            time = sel.xpath("./span/text()").extract()[0].replace("[", "").replace("]", "")
            guide_item["title"] = title
            guide_item["href"] = href
            guide_item["time"] = time
            yield guide_item
        page_sel = response.xpath("//div[@class='pager']")
        if page_sel:
            directions = page_sel.xpath("./a")
            for direction in directions:
                if direction.xpath("./text()").extract()[0] == u"下一页":
                    next_page_url = self.base_url + direction.xpath("./@href").extract()[0]
                    yield scrapy.Request(next_page_url, callback=self.parse_aspect)
                    break
