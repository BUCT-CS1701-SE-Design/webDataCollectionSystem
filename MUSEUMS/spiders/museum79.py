# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem
class Museum79Spider(scrapy.Spider):
    name = 'museum79'
    allowed_domains = ['kfsbwg.com']
    start_urls = ['http://www.kfsbwg.com/'] 
    # 设置经过哪个pipeline去处理
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
    def parse(self, response):
        item = MuseumsItem()
        item['museumID']=79
        item['museumName']='开封博物馆'
        item['Location']=response.xpath('//*[@id="foot_wz"]/p/text()[2]').get().strip()+response.xpath('//*[@id="foot_wz"]/p/text()[3]').get().strip()
        Link='http://www.kfsbwg.com/'
        item['Link']=Link
        url1=response.xpath("//div[@class='r']//area[1]/@href").extract()
        url1[0]='http://www.kfsbwg.com/'+str(url1[0])
        yield scrapy.Request(url1[0],callback=self.Opentime,meta={"item":item})
    def Opentime(self,response):
        opentime=response.xpath("//*[@id='list']/div[2]//p/span/span/text()").getall()
        opentime="".join(opentime).strip()
        item=response.meta["item"]
        item['opentime']=opentime
        url=response.xpath('//*[@id="nav"]/ul/li[3]/a/@href').extract()
        url[0]='http://www.kfsbwg.com/'+str(url[0])
        yield scrapy.Request(url[0],callback=self.Others,meta={"item":item})
    def Others(self,response):
        telephone_p =response.xpath("//*[@id='foot_wz']/p/text()[4]").get().strip().split("：",1)
        telephone=telephone_p[1]
        item=response.meta["item"]
        item['telephone']=telephone
        aa=response.xpath("//*[@id='Map']/area[1]/@href").extract()
        aa[0]='http://www.kfsbwg.com/'+str(aa[0])
        yield scrapy.Request(aa[0],callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        introduction=response.xpath("//*[@id='list']/div[2]/div/text()").getall()
        introduction="".join(introduction).strip()
        item=response.meta["item"]
        item['introduction']=introduction
        yield item 








        
    

        
        
