import scrapy

from MUSEUMS.items import MuseumsItem
class Museum82Spider(scrapy.Spider):
    name = 'museum82'
    allowed_domains = ['jzmsm.org']
    start_urls = ['http://www.jzmsm.org/yk/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=82
        item['museumName'] = '荆州博物馆'
        item['Link']='http://www.jzmsm.org/'
        opentime=response.xpath("//div[@class='yk_foot']//td[2]/text()[1]").getall()
        item['opentime']="".join(opentime).strip()
        others=response.xpath("//div[@class='yk_foot']//td[2]/text()[2]").getall()
        some="".join(others).strip().split()
        item['Location']=some[1]
        item['telephone']=some[3]
        url='http://www.jzmsm.org'+response.xpath("//div[@class='yk_r']/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):  
        item=response.meta["item"]
        url='http://www.jzmsm.org'+response.xpath("//div[@class='menu']//ul/li[6]/ul/li[1]/a/@href").extract_first()+'zongshu/2017-08-21/1100.html'
        yield scrapy.Request(url,callback=self.Introduce,meta={"item":item})
    def Introduce(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//div[@class='mian']/div/div[3]/p/span/text()").getall()
        introduction="".join(introduction).strip()
        item['introduction']=introduction
        yield item