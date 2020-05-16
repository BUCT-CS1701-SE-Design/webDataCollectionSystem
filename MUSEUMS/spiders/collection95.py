import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection95Spider(scrapy.Spider):
    name = 'collection95'
    allowed_domains = ['gzchenjiaci.com']
    start_urls = ['http://www.gzchenjiaci.com/MYwebsite/rc/my_index.htm'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=95
        pass