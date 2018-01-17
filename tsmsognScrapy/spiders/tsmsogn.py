# -*- coding: utf-8 -*-
import scrapy


class TsmsognSpider(scrapy.Spider):
    name = 'tsmsogn'
    allowed_domains = ['tsmsogn.github.io']
    start_urls = ['http://tsmsogn.github.io/']

    def parse(self, response):
        pass
