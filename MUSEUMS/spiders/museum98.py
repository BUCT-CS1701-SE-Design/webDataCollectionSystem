import scrapy

from MUSEUMS.items import MuseumsItem
class Museum98Spider(scrapy.Spider):
    name = 'museum98'
    allowed_domains = ['hainanmuseum.org']
    start_urls = ['http://www.hainanmuseum.org/hbgk/jj'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=98
        item['museumName'] = '海南省博物馆'
        introduction=response.xpath("//div[@class='article']/span/text()").getall()
        item['introduction']="".join(introduction).strip()
        url='http://www.hainanmuseum.org/'
        item['Link']=url
        yield scrapy.Request(url,callback=self.Other,meta={"item":item})
    def Other(selg,response):
        item=response.meta["item"]
        item['opentime']=response.xpath("//p[@class='newList']/text()[3]").get().strip()
        Location=response.xpath("//p[@class='about fix']//text()[3]").get().strip().split("邮",1)
        item['Location']=Location[0]
        item['telephone']=response.xpath("//p[@class='newList']/text()[7]").get().strip()
        yield item