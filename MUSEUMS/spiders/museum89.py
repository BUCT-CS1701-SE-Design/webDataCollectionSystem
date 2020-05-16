import scrapy

from MUSEUMS.items import MuseumsItem
class Museum88Spider(scrapy.Spider):
    name = 'museum89'
    allowed_domains = ['chinajiandu.cn']
    start_urls = ['http://www.chinajiandu.cn/News/Details/bgjs'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=89
        item['museumName'] = '长沙简牍博物馆'
        introduction=response.xpath("//div[@class='cont']//text()").getall()
        item['introduction']="".join(introduction).strip()
        item['Link']='http://www.chinajiandu.cn/'
        item['Location']=response.xpath("//div[@class='box']/p[1]/text()").get()
        item['telephone']=response.xpath("//div[@class='box']/p[2]/text()").get()
        url='http://www.chinajiandu.cn/'+response.xpath("//div[@class='allcenter']//ul[@class='menu normalfont']/li[1]/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Opent,meta={"item":item})
    def Opent(self,response):
        item=response.meta["item"]
        url1='http://www.chinajiandu.cn/'+response.xpath("//ul[@class='services']/li[1]/a/@href").extract_first()
        yield scrapy.Request(url1,callback=self.Opentime,meta={"item":item})
    def Opentime(self,response):
        item=response.meta["item"]
        item['opentime']=response.xpath("//div[@class='cont']/p[3]/text()").get().strip()
        yield item