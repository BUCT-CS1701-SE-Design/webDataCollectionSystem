import scrapy

from MUSEUMS.items import MuseumsItem
class Museum102Spider(scrapy.Spider):
    name = 'museum102'
    allowed_domains = ['clg.dxpgl.cn']
    start_urls = ['http://clg.dxpgl.cn/service-notice.html?dxpglclgkffwkf'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=102
        item['museumName'] = '邓小平故居陈列馆'
        item['opentime']='园区每周二至周日8：30—17：00对外开放；周一闭馆不闭园（国家法定假日除外）。'
        item['Link']='http://clg.dxpgl.cn/'
        item['Location']=response.xpath("//div[@class='clearfix']/text()[1]").get().strip()
        item['telephone']=response.xpath("//div[@class='clearfix']/text()[2]").get().strip()
        url='http://clg.dxpgl.cn'+response.xpath("//div[@class='foot_link']/a[1]/@href").get()
        yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//div[@class='firstmusem']/text()").getall()
        item['introduction']="".join(introduction).strip()
        yield item