# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = ['https://www.amazon.com/books-used-books-textbooks/b/?ie=UTF8&node=283155&ref_=topnav_storetab_b']

    def parse(self, response):
        items = AmazonItem()

        p_name = response.css('a.acs-product-block__product-title > span > span::text').extract()
        p_author = response.css('span.acs-product-block__contributor > span::text').extract()
        p_price = response.css('.a-price-whole::text').extract()
        p_link = response.css('.acswidget-carousel .acs-product-block__product-image img::attr(src)').extract()

        items['p_name'] = p_name
        items['p_author'] = p_author
        items['p_price'] = p_price
        items['p_link'] = p_link

        yield items
