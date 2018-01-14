# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FaqItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    answer = scrapy.Field()
    href = scrapy.Field()

