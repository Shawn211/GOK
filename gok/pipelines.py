# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from gok.settings import IMAGES_STORE
from scrapy.exceptions import DropItem
from scrapy import Request
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class GokPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        ename=item['ename']
        cname=item['cname']
        skins=item['skins']

        skin=skins.split('|')
        for image_name in skin:
            image_url='http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'+str(ename)+'/'+str(ename)+'-bigskin-'+str(skin.index(image_name)+1)+'.jpg'
            yield Request(image_url,meta={'item':item, 'cname':cname, 'skin':skin, 'num':skin.index(image_name)})

    def item_completed(self,results,item,info):      #最后执行
        image_path=[x['path'] for ok,x in results if ok]
        if not image_path:
            raise DropItem('图片下载失败：%s'%image_path)

    def file_path(self,request,response=None,info=None):
        #item虽然来自当前的item，但是以防万一，单独将需要的数据信息传送过来，此处就会出现item配对错误
        item=request.meta['item']
        num=request.meta['num']
        skin=request.meta['skin']
        cname=request.meta['cname']

        image_guid=skin[num].decode('utf-8')+'.jpg'
        filename=cname.decode('utf-8')+'/'+image_guid
        return filename
