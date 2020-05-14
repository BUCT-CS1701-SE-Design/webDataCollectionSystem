import scrapy

from MUSEUMS.items import MuseumsItem
class Museum101Spider(scrapy.Spider):
    name = 'museum101'
    allowed_domains = ['wuhouci.net.cn']
    start_urls = ['http://www.wuhouci.net.cn/about.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=101
        item['museumName'] = '成都武侯祠博物馆'
        introduction=response.xpath("//div[@class='aboutBox boxWidth']//text()").getall()
        item['introduction']="".join(introduction).strip().replace('\t\r\n','').replace('\t','').replace('\r','')
        item['Link']='http://www.wuhouci.net.cn/'
        url='http://www.wuhouci.net.cn/visit-ticket.html'
        yield scrapy.Request(url,callback=self.Other,meta={"item":item})
    def Other(self,response):
        item=response.meta["item"]  
        opentime=response.xpath("//section[@class='ticketTop']//text()[2]").getall()
        item['opentime']=opentime[1].strip()
        item['Location']='中国.成都市武侯祠大街231号'
        item['telephone']='+86-028-85552397(业务)、85535951(票务)、85593818(网站)'
        yield item