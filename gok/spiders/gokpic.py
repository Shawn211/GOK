# -*- coding: utf-8 -*-
import scrapy
import json
from gok.items import GokItem

class GokpicSpider(scrapy.Spider):
    name = 'gokpic'
    allowed_domains = ['pvp.qq.com/web201605/herolist.shtml','pvp.qq.com/web201605/herodetail']
    start_urls = ['http://pvp.qq.com/web201605/herodetail/501.shtml']

    def parse(self, response):
        item={}
        item=GokItem()

        body = response.body.lstrip('[').rstrip(']')
        herolist = body.split(', ')
        for hero in herolist:
            hero=json.loads(hero)

        item['hero']=herolist
        yield item
