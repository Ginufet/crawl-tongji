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


class DownloadsItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    href = scrapy.Field()


class AnnouncementItem(scrapy.Item):
    title = scrapy.Field()


class GuideItem(scrapy.Item):
    title = scrapy.Field()
    time = scrapy.Field()
    href = scrapy.Field()
