# -*- coding: utf-8 -*-
import scrapy
from tsmsognScrapy.items import TsmsognscrapyItem


class TsmsognSpider(scrapy.Spider):
    name = 'tsmsogn'
    allowed_domains = ['tsmsogn.github.io']
    start_urls = ['http://tsmsogn.github.io/']

    def parse(self, response):
        self.logger.info("Scraping: " + response.url)

        item = TsmsognscrapyItem()
        item['url'] = response.url
        item['status'] = response.status
        item['title'] = response.selector.xpath('//title/text()').extract_first()
        yield item

        for href in response.xpath('//a/@href').extract():
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse)
