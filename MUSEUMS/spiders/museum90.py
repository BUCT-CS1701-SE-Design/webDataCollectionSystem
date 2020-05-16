import scrapy

from MUSEUMS.items import MuseumsItem
class Museum90Spider(scrapy.Spider):
    name = 'museum90'
    allowed_domains = ['gdmuseum.com']
    start_urls = ['http://www.gdmuseum.com/gdmuseum/_300882/_300886/index.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=90
        item['museumName'] = '广东省博物馆'
        opentime=response.xpath("//ul[@class='list_ul']/li[1]//div[@class='summary']/text()").get().strip().split('。',1)
        item['opentime']=opentime[0]
        item['Link']='http://www.gdmuseum.com/'
        item['Location']=response.xpath("//div[@class='foot_right']/p[1]/text()").get()
        item['telephone']=response.xpath("//div[@class='foot_center2']/p[1]/span[1]/text()").get()
        url='http://www.gdmuseum.com/'+response.xpath("//li[@class='nli'][2]//li[1]/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//div[@class='detail_cont']/p/text()").getall()
        item['introduction']="".join(introduction).strip()
        yield item