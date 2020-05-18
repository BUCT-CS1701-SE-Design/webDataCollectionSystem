import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection100Spider(scrapy.Spider):
    name = 'collection100'
    allowed_domains = ['sxd.cn']
    start_urls = ['http://www.sxd.cn/list_2.asp?bigclass=29&smallclass=1','http://www.sxd.cn/list_2.asp?bigclass=29&smallclass=2','http://www.sxd.cn/list_2.asp?bigclass=29&smallclass=3','http://www.sxd.cn/list_2.asp?bigclass=29&smallclass=4'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=100
        lilist=response.xpath("//div[@class='picout']")
        for li in lilist:
            collectionName=li.xpath(".//a/@title").get().strip()
            # collectionIntroduction=''
            collectionImage='http://www.sxd.cn/'+li.xpath(".//img/@src").get()
            item['collectionName']=collectionName
            item['collectionIntroduction']=''
            item['collectionImage']=collectionImage
            yield item