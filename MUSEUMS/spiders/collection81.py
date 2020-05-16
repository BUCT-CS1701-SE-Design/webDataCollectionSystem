# import scrapy
# import re
# from MUSEUMS.items import collection75Item
# class Collection80Spider(scrapy.Spider):
#     name = 'collection81'
#     allowed_domains = ['hbww.org']
#     start_urls = ['http://www.hbww.org/Views/CollectionIndex.aspx?PNo=Collection&No=Collection&type=Default']
#     custom_settings={
#         'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4,}
#     }
#     def parse(self, response):
#         item=collection75Item()
#         item['museumID']=81
#         print("*"*10)
#         url1=response.xpath("//map[@id='Map']//@href").extract()
#         for url in url1:
#             url='http://www.hbww.org/'+url
#             yield scrapy.Request(url,callback=self.Others,meta={"item":item})
#     def Others(self,response):
#         item=response.meta["item"]
#         url2='http://www.hbww.org/'+response.xpath("//ul[@id='ulImageList']/li[1]/a/@href").get()
#         yield scrapy.Request(url2,callback=self.Other,meta={"item":item})
#     def Other(self,response):
#         item=response.meta["item"]
#         item['collectionName']=response.xpath("//div[@class='agdetail_r']/h3/text()").get().strip()
#         collectionIntroduction=response.xpath("//div[@class='jspPane']/p/text()").getall()
#         item['collectionImage']=response.xpath("//div[@class='agdetailimg']/a/img/@src").get()
#         item['collectionIntroduction']="".join(collectionIntroduction).strip()
#         print(item)