import scrapy
from MUSEUMS.items import collection75Item

class Collection79Spider(scrapy.Spider):
    name = 'collection79'
    allowed_domains = ['kfsbwg.com']
    start_urls = ['http://www.kfsbwg.com/html/wenwu/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item['museumID']=79
        lurl=response.xpath('//*[@id="r_ww"]/a/@href').extract()
        for url in lurl:
            url='http://www.kfsbwg.com'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})

    def Others(self,response):
        li_list=response.xpath("//*[@id='r_ww']/ul/li")
        item=response.meta["item"]
        for li in li_list:
            collectionName=li.xpath('./p/a/text()').get()
            item['collectionName']=collectionName
            collectionIntroduction=li.xpath("./a/@href").get()
            item['collectionIntroduction']=collectionIntroduction
            collectionImage=li.xpath("./a/img/@src").get()
            item['collectionImage']=collectionImage
            yield item
