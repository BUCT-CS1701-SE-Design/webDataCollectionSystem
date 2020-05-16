import scrapy
from MUSEUMS.items import MuseumsItem
class Museum84Spider(scrapy.Spider):
    name = 'museum84'
    allowed_domains = ['1911museum.com']
    start_urls = ['http://www.1911museum.com/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=84
        item['museumName'] ='辛亥革命武昌起义纪念馆' 
        item['opentime']=response.xpath("//div[@class='service']/div/p[1]//text()").get()
        item['Link']='http://www.1911museum.com/'
        item['Location']=response.xpath("//div[@class='service']/div/p[4]/text()").get()
        telephone_p =response.xpath("//div[@class='service']/div/p[5]/text()").get().strip().split("：",1)
        item['telephone']=telephone_p[1]
        url='http://www.1911museum.com'+response.xpath("//ul[@class='menu']/li[2]/ul/li[1]/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        introduction=response.xpath("//div[@class='cont']/p/text()").getall()
        item=response.meta["item"]
        item['introduction']="".join(introduction).strip()
        yield item