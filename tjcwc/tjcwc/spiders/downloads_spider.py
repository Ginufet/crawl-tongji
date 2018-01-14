# -*- coding: utf-8 -*-
import scrapy
from tjcwc.items import DownloadsItem


class DownloadsSpider(scrapy.Spider):
    name = 'downloads'
    allowed_domains = ["tongji.edu.cn"]
    base_url = "http://tjcwc.tongji.edu.cn/"
    start_urls = [
        "http://tjcwc.tongji.edu.cn/index.php?classid=9735"
    ]

    def parse(self, response):
        for aspect_url_sel in response.xpath("//li[@class='depth_1']/a/@href"):
            aspect_url = self.base_url + aspect_url_sel.extract()
            yield scrapy.Request(aspect_url, callback=self.parse_aspect)

    def parse_aspect(self, response):
        for sel in response.xpath("//div[@class='download_file_list']/ul/li"):
            downloads_item = DownloadsItem()
            title = sel.xpath("./a/text()").extract()[0].replace("\n","").replace(" ", "")
            href = self.base_url + "index.php" + sel.xpath("./a/@href").extract()[0]
            downloads_item["title"] = title
            downloads_item["href"] = href
            downloads_item["time"] = sel.xpath("./span/text()").extract()[0].replace("[", "").replace("]", "")
            yield downloads_item
        page_sel = response.xpath("//div[@class='pager']")
        if page_sel:
            directions = page_sel.xpath("./a")
            for direction in directions:
                if direction.xpath("./text()").extract()[0] == u"下一页":
                    next_page_url = self.base_url + direction.xpath("./@href").extract()[0]
                    yield scrapy.Request(next_page_url, callback=self.parse_aspect)
                    break
