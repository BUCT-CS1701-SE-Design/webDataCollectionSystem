# import scrapy
# from MUSEUMS.items import exhibition75Item
# class Exhibition83Spider(scrapy.Spider):
#     name = 'exhibition83'
#     allowed_domains = ['whmuseum.com.cn']
#     start_urls = ['http://www.whmuseum.com.cn/collection'] 
    
#     def parse(self, response):
#         item=exhibition75Item()
#         item["museumID"]=83
#         # exhibitionTime=
#         # item['exhibitionTheme']=response.xpath("//div[@id='D1pic1']/div/a/@title").get().strip()
#         # item['exhibitionIntroduction']=response.xpath("//div[@class='xlzl_intro fr']/text()").get().strip()
#         # item['exhibition_picture']='http://www.eywsqsfbwg.com/'+response.xpath("//div[@id='D1pic1']/div/a/img/@src").get()
#         yield item   