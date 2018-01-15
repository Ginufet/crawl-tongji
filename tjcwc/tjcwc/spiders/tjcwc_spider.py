# -*- coding: utf-8 -*-

import scrapy
import abc


class TjcwcSpider(scrapy.Spider):

    __metaclass__ = abc.ABCMeta

    allowed_domains = ["tongji.edu.cn"]
    base_url = "http://tjcwc.tongji.edu.cn/"
