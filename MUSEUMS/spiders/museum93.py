import scrapy

from MUSEUMS.items import MuseumsItem
class Museum93Spider(scrapy.Spider):
    name = 'museum93'
    allowed_domains = ['shenzhenmuseum.com/']
    start_urls = ['https://www.shenzhenmuseum.com/aboutus/index?type=about&curIndex=0'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=93
        item['museumName'] = '深圳博物馆'
        introduction=response.xpath("//div[@class='aboutUsTextTabs']/div[1]/div//p/text()").getall()
        item['introduction']="".join(introduction).strip()
        item['Link']='https://www.shenzhenmuseum.com/'
        item['Location']='广东省深圳市福田区福中路市民中心A区'
        opentime=response.xpath("//div[@class='visit-service']//p[1]/text()").get().strip().split(":",1)
        item['opentime']=opentime[1]
        telephone=response.xpath("//div[@class='aboutUsTextTabs']/div[6]/p[9]//text()").get().strip().split("(",1)
        telephone+=response.xpath("//div[@class='aboutUsTextTabs']/div[6]/p[19]//text()").get().strip().split("(",1)
        telephone+=response.xpath("//div[@class='aboutUsTextTabs']/div[6]/p[24]//text()").get().strip().split("(",1)
        item['telephone']=telephone[0]
        yield item
        
        