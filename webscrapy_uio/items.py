# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapyUioItem(scrapy.Item):
    name = scrapy.Field()  # hidden-xs hidden-tiny col-xs-1 pokenumber
    model = scrapy.Field()  # font-size:18px
    price = scrapy.Field()  # iv
    diference = scrapy.Field()  # cp
