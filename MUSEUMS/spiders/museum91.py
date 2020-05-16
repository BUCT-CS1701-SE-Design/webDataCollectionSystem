import scrapy

from MUSEUMS.items import MuseumsItem
class Museum91Spider(scrapy.Spider):
    name = 'museum91'
    allowed_domains = ['gznywmuseum.org']
    start_urls = ['https://www.gznywmuseum.org/nbjj/index.jhtml'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=91
        item['Link']='https://www.gznywmuseum.org/'
        item['museumName'] = '西汉南越王博物馆'
        introduction=response.xpath("//div[@class='synopsis-detail-content-text']/p/text()").getall()
        item['introduction']="".join(introduction).strip()
        item['opentime']=response.xpath("//div[@class='synopsis-detail-content-info']/p[3]/text()").get()+response.xpath("//div[@class='synopsis-detail-content-info']/p[4]/text()").get()
        item['Location']=response.xpath("//div[@class='synopsis-detail-content-info']/p[1]/text()").get()
        telephone=response.xpath("//div[@class='synopsis-detail-content-info']/p[5]/text()").get().strip().split()
        item['telephone']=telephone[0]
        yield item