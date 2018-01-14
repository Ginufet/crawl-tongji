# -*- coding: utf-8 -*-
import scrapy
from tjcwc.items import FaqItem


class FaqSpider(scrapy.Spider):
    name = "faq"
    allowed_domains = ["tongji.edu.cn"]
    start_urls = [
        "http://tjcwc.tongji.edu.cn/index.php?classid=9778",
    ]
    base_url = "http://tjcwc.tongji.edu.cn/"

    def parse(self, response):
        for aspect_url_sel in response.xpath("//li[@class='depth_1']/a/@href"):
            aspect_url = self.base_url + aspect_url_sel.extract()
            print aspect_url
            yield scrapy.Request(aspect_url, callback=self.parse_aspect)

    def parse_aspect(self, response):
        for sel in response.xpath("//div[@class='news_list']/ul/li"):
            faq_item = FaqItem()
            title = sel.xpath("./a/text()").extract()[0].replace(u"请问", u"")
            href = self.base_url + sel.xpath("./a/@href").extract()[0]
            faq_item["title"] = title
            faq_item["href"] = href
            faq_item["time"] = sel.xpath("./span/text()").extract()[0].replace("[", "").replace("]", "")
            yield scrapy.Request(href, meta={"item": faq_item}, callback=self.parse_answer)

    def parse_answer(self, response):
        faq_item = response.meta["item"]
        answers = response.xpath("//table/tr/td[@class='news_content']/p/span/text()").extract()
        answer = ''.join(answers).replace(u'答：', u'')
        faq_item["answer"] = answer
        return faq_item



