import scrapy

from MUSEUMS.items import MuseumsItem
class Museum100Spider(scrapy.Spider):
    name = 'museum100'
    allowed_domains = ['sxd.cn']
    start_urls = ['http://www.sxd.cn/showinfo.asp?id=18'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=100
        item['museumName'] = '三星堆博物馆'
        item['Link']='http://www.sxd.cn/'
        item['Location']='四川省广汉市三星堆镇'
        tele=response.xpath("//div/table[4]//td[@align='center']/text()").get().strip().split()
        item['telephone']=tele[1]
        opentime=response.xpath("//td[@valign='top']//tr[2]/td/p[7]//text()").getall()+response.xpath("//td[@valign='top']//tr[2]/td/p[8]//text()").getall()
        item['opentime']="".join(opentime).strip()
        url='http://www.sxd.cn/showinfo.asp?id=1526&bigclass=5'
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//td[@valign='top']//tr[2]//p/text()").getall()
        item['introduction']="".join(introduction).strip().replace('\t','').replace('\r\n','')
        yield item