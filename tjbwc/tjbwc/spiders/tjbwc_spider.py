# -*- coding: utf-8 -*-
import scrapy
from abc import ABCMeta


class TjbwcSpider(scrapy.Spider):

    __metaclass__ = ABCMeta

    allowed_domain = ["tongji.edu.cn"]
    base_url = "http://baowei.tongji.edu.cn"
