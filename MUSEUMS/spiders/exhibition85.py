# import scrapy
# from MUSEUMS.items import exhibition75Item
# class Exhibition85Spider(scrapy.Spider):
#     name = 'exhibition85'
#      allowed_domains = ['zhongshanwarship.org.cn']
#     start_urls = ['http://www.zhongshanwarship.org.cn/wenwu.html'] 
    
#     def parse(self, response):
#         item=exhibition75Item()
#         item["museumID"]=85
#         # exhibitionTime=
#         item['exhibitionTheme']=response.xpath("//div[@id='D1pic1']/div/a/@title").get().strip()
#         item['exhibitionIntroduction']=response.xpath("//div[@class='xlzl_intro fr']/text()").get().strip()
#         item['exhibition_picture']='http://www.eywsqsfbwg.com/'+response.xpath("//div[@id='D1pic1']/div/a/img/@src").get()
#         yield item   