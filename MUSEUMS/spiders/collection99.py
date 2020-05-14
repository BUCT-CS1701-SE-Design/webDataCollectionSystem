import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection99Spider(scrapy.Spider):
    name = 'collection99'
    allowed_domains = ['zdm.cn']
    start_urls = ['http://www.zdm.cn/introduceinfo.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=99
        collectionName='暂无'
        collectionIntroduction='暂无'
        collectionImage='暂无'
        item['collectionName']=collectionName
        item['collectionIntroduction']=collectionIntroduction
        item['collectionImage']=collectionImage
        yield item