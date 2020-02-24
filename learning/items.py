# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PyCoderItem(scrapy.Item):
        title = scrapy.Field()
        date = scrapy.Field()
        text = scrapy.Field()
        picture = scrapy.Field()
        link = scrapy.Field()