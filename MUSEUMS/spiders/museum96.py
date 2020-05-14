import scrapy

from MUSEUMS.items import MuseumsItem
class Museum96Spider(scrapy.Spider):
    name = 'museum96'
    allowed_domains = ['gxmuseum.cn']
    start_urls = ['http://www.gxmuseum.cn/a/introduction/index2.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=96
        item['museumName'] = '广西壮族自治区博物馆'
        introduction=response.xpath("//div[@class='content']//p/text()").getall()
        item['introduction']=str(introduction[3].strip())+str(introduction[4].strip())+str(introduction[5].strip())+str(introduction[6].strip())+str(introduction[7].strip())
        url ='http://www.gxmuseum.cn/'+response.xpath("//li[@id='s_11']/a[1]/@href").get()
        yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        opentime=response.xpath("//div[@id='service']/div[1]/p[1]/text()[1]").get().strip().split()
        item['opentime']=opentime[0]
        item['Link']='http://www.gxmuseum.cn/'
        Location=response.xpath("//p[@class='powered']/text()").get().strip().split()
        item['Location']=Location[1]
        telephone=response.xpath("//div[@id='service']/div[6]/p[23]/text()").get().strip().split("：",1)
        item['telephone']=telephone[1]
        yield item
