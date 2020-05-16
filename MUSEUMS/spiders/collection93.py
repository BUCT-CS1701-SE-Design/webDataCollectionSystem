import scrapy
import re
from MUSEUMS.items import collection75Item
class Collection93Spider(scrapy.Spider):
    name = 'collection93'
    allowed_domains = ['shenzhenmuseum.com/']
    start_urls = ['https://www.shenzhenmuseum.com/webCollection'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=93
        url1=response.xpath("//div[@class='wrap']/div//div[2]//a/@href").getall()
        for url in url1:
            url='https://www.shenzhenmuseum.com'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item}, dont_filter=True)
    def Others(self,response):
        item=response.meta["item"]
        collectionName=response.xpath("//div[@id='detailInfo']/h2/text()").get().strip()
        collectionIntroduction=response.xpath("//div[@id='detailInfo']//p//text()").getall()
        collectionImage=response.xpath("//ul[@id='dataList1']/li[1]/a/img/@src").get()
        item['collectionName']=collectionName
        item['collectionIntroduction']="".join(collectionIntroduction).strip()
        item['collectionImage']=collectionImage
        yield item