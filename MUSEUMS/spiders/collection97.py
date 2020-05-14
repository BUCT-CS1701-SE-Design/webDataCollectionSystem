import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection97Spider(scrapy.Spider):
    name = 'collection97'
    allowed_domains = ['amgx.org']
    start_urls = ['http://www.amgx.org/boutique.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=97
        url1=response.xpath("//div[@class='videoli']/dl")
        for li in url1:
            url='http://www.amgx.org/'+li.xpath("./dd//@href").get()
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        # collectionName=response.xpath("//h2[@class='newstit']/text()").get().strip()
        collectionIntroduction=response.xpath("//td[@colspan='3']//text()").getall()
        collectionImage='http://www.amgx.org'+response.xpath("//div[@id='pic']/img/@src").get()
        # item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip().split("撰稿人",1)[0].strip()
        item['collectionImage']=collectionImage
        item['collectionName']=response.xpath("//td[@align='center']/text()").get()
        yield item