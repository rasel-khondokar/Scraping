# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    p_name = scrapy.Field()
    p_author = scrapy.Field()
    p_price = scrapy.Field()
    p_link = scrapy.Field()
    pass
