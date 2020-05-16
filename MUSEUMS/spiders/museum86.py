import scrapy

from MUSEUMS.items import MuseumsItem
class Museum86Spider(scrapy.Spider):
    name = 'museum86'
    allowed_domains = ['hnmuseum.com']
    start_urls = ['http://www.hnmuseum.com/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=86
        item['museumName'] = '湖南省博物馆'
        item['opentime']=response.xpath("//*[@id='block-block-27']/div/div[3]/ul/li[1]/p/span/text()").get().strip()
        item['Link']='http://www.hnmuseum.com/'
        item['Location']=response.xpath("//*[@id='block-block-27']/div/div[3]/ul/li[3]/p/text()[2]").get().strip()
        item['telephone']=response.xpath("//*[@id='block-block-27']/div/div[3]/ul/li[3]/p/text()[1]").get().strip()
        url='http://www.hnmuseum.com/'+response.xpath("//*[@id='block-menu-block-1']/div/div/ul/li[2]/ul/li[1]/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//*[@id='node-3']/div/div[2]/div/div/p/text()").getall()
        item['introduction']="".join(introduction).strip()
        yield item