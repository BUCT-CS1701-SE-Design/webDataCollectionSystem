import scrapy

from MUSEUMS.items import MuseumsItem
class Museum103Spider(scrapy.Spider):
    name = 'museum103'
    allowed_domains = ['cddfct.com']
    start_urls = ['http://www.cddfct.com/info/show/id/8/Tpls/w4'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=103
        item['museumName'] = '成都杜甫草堂博物馆'
        introduction=response.xpath("//div[@id='simTestContent']//text()").getall()
        item['introduction']="".join(introduction).strip()
        url=response.xpath("//div[@class='po']/a[2]/@href").get()
        yield scrapy.Request(url,callback=self.Fir,meta={"item":item})
    def Fir(self,response):
        item=response.meta["item"]
        url1=response.xpath("//div[@class='index_sever']/ul/li[1]/a/@href").get()
        yield scrapy.Request(url,callback=self.Other,meta={"item":item})
    def Other(self,response):
        item=response.meta["item"]
        item['opentime']=response.xpath("//ul[@class='co']//p[5]//text()").get().strip()+response.xpath("//ul[@class='co']//p[6]//text()").get().strip()
        item['Link']='http://www.cddfct.com/'
        location=response.xpath("//div[@class='copyright']/p[3]/text()[1]").get().strip().split("网",1)
        item['Location']=location[0]
        item['telephone']=response.xpath("//ul[@class='co']//p[12]//text()").get().strip()
        yield item