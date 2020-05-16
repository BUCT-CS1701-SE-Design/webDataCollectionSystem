import scrapy

from MUSEUMS.items import MuseumsItem
class Museum104Spider(scrapy.Spider):
    name = 'museum104'
    allowed_domains = ['scmuseum.cn']
    start_urls = ['http://www.scmuseum.cn/list-1714.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=104
        item['museumName'] = '四川博物院'
        introduction=response.xpath("//div[@class='sbp-content']/p/text()").getall()
        item['introduction']="".join(introduction).strip()
        item['opentime']=response.xpath("//div[@class='quote-map']/text()[1]").get().strip()
        item['Link']='http://www.scmuseum.cn/'
        others=response.xpath("//div[@class='quote-map']/text()[2]").get()
        location=others.split("9",1)
        item['Location']=location[1]
        tele=others.split("馆",1)
        item['telephone']=tele[0]
        yield item