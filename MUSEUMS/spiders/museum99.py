import scrapy

from MUSEUMS.items import MuseumsItem
class Museum99Spider(scrapy.Spider):
    name = 'museum99'
    allowed_domains = ['zdm.cn']
    start_urls = ['http://www.zdm.cn/introduceinfo.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=99
        item['museumName'] = '自贡恐龙博物馆'
        introduction=response.xpath("//div[@class='textBox']//text()").getall()
        item['introduction']="".join(introduction).strip()
        url='http://www.zdm.cn/'
        item['Link']=url
        yield scrapy.Request(url,callback=self.Other,meta={"item":item})
    def Other(self,response):
        item=response.meta["item"]
        opentime=response.xpath("//div[@class='box']/ul//text()").getall()
        item['opentime']="".join(opentime).strip().replace('\r\n','')
        item['Location']='四川省自贡市的东北部，距市中心11公里'
        item['telephone']=response.xpath("//p[@class='footerTel']//text()").get()
        yield item