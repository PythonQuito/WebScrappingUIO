# -*- coding: utf-8 -*-
import scrapy
from webscrapyuio.items import WebscrapyUioItem
from scrapy.selector import Selector

class PyuioPypizzaSpider(scrapy.Spider):
    name = 'pyuio_pypizza'
    allowed_domains = ['https://www.apple.com/shop/refurbished/mac/macbook-pro']
    start_urls = ['http://https://www.apple.com/shop/refurbished/mac/macbook-pro/']

    def parse(self, response):
        item = WebscrapyUioItem()

        selector = Selector(response)
        item['name'] = selector.xpath("//div//ul//li//h3//a/text()").extract()
        item['price'] = selector.xpath("//div//ul//li//div[@class='as-price-currentprice as-producttile - currentprice']/text()").extract()
        item['diference'] = selector.xpath("//div//ul//li//span[@class='as-producttile-savingsprice']/text()").extract()
        item['model'] = ''
        response
