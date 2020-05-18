import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection94Spider(scrapy.Spider):
    name = 'collection94'
    allowed_domains = ['guangzhoumuseum.cn']
    start_urls = ['http://www.guangzhoumuseum.cn/main.asp'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
       pass