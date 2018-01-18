# -*- coding: utf-8 -*-
import scrapy
import json
from gok.items import GokItem

class GokpicSpider(scrapy.Spider):
    name = 'gokpic'
    allowed_domains = ['pvp.qq.com/web201605/herolist.shtml','pvp.qq.com/web201605/herodetail']
    start_urls = ['http://pvp.qq.com/web201605/js/herolist.json']

    def parse(self, response):
        item={}
        item=GokItem()

        body = response.body.lstrip('[').rstrip(']')
        herolist = body.split(', ')

        for hero in herolist:
            hero=json.loads(hero)
            item['ename']=hero['ename']
            item['cname']=hero['cname'].decode('utf-8')
            item['skins']=hero['skin_name']
            yield item
