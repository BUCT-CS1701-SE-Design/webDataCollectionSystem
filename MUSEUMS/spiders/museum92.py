import scrapy

from MUSEUMS.items import MuseumsItem
class Museum92Spider(scrapy.Spider):
    name = 'museum92'
    allowed_domains = ['sunyat-sen.org']
    start_urls = ['http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=141'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=92
        item['museumName'] = '孙中山故居纪念馆'  
        item['opentime']=response.xpath("//div[@class='contentBox']/p[2]/text()").get()
        item['Link']='http://www.sunyat-sen.org/'
        item['Location']='广东省中山市翠亨大道93号'
        telephone=response.xpath("//div[@class='contentBox']/p[16]/text()").get().strip().split("：",1)
        item['telephone']=telephone[1]
        url=response.xpath("//ul[@class='Nav_1']/li[2]/ul/li[1]/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//div[@class='contentBox']/p/text()").getall()
        item['introduction']="".join(introduction).strip()
        yield item