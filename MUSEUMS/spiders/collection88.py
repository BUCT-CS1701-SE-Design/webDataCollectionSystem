# import scrapy
# import re
# from MUSEUMS.items import collection75Item
# class Collection88Spider(scrapy.Spider):
#     name = 'collection88'
#     allowed_domains = ['shaoqiguli.com']
#     start_urls = ['http://www.shaoqiguli.com/'] 
#     # custom_settings={
#     #     'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
#     # }
#     def parse(self, response):
#         item=collection75Item()
#         item['museumID']=88
#         url1=response.xpath("//ul[@class='of']/li/a/@href").getall()
#         for url in url1:
#             yield scrapy.Request(url,callback=self.Others,meta={"item":item})
#     def Others(self,response):
#         item=response.meta["item"]
#         collectionName=response.xpath("//h2[@class='newstit']/text()").get().strip()
#         collectionIntroduction=response.xpath("//div[@id='conbox']//text()").getall()
#         collectionImage='http://www.eywsqsfbwg.com/'+response.xpath("//div[@id='conbox']/img/@src").get()
#         item['collectionName']=collectionName
#         item['collectionIntroduction']="".join(collectionIntroduction).strip()
#         item['collectionImage']=collectionImage
#         yield item