# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TjcwcItem(scrapy.item):
    title = scrapy.Field()
    time = scrapy.Field()
    href = scrapy.Field()


class FaqItem(TjcwcItem):
    answer = scrapy.Field()
