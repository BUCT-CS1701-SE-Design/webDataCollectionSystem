import scrapy

from MUSEUMS.items import MuseumsItem
class Museum103Spider(scrapy.Spider):
    name = 'museum103'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E6%88%90%E9%83%BD%E6%9D%9C%E7%94%AB%E8%8D%89%E5%A0%82%E5%8D%9A%E7%89%A9%E9%A6%86/4824775?fr=aladdin'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=103
        item['museumName'] = '成都杜甫草堂博物馆'
        introduction=response.xpath("//div[@class='para']//text()").getall()
        item['introduction']=introduction
    #     url=response.xpath("//div[@class='po']/a[2]/@href").get()
    #     yield scrapy.Request(url,callback=self.Fir,meta={"item":item})
    # def Fir(self,response):
    #     item=response.meta["item"]
    #     url1=response.xpath("//div[@class='index_sever']/ul/li[1]/a/@href").get()
    #     yield scrapy.Request(url,callback=self.Other,meta={"item":item})
    # def Other(self,response):
    #     item=response.meta["item"]
        item['opentime']='(5月~10月）：8:00~18:30 （11月~次年4月）：8:00~18:00'
        # response.xpath("//ul[@class='co']//p[5]//text()").get().strip()+response.xpath("//ul[@class='co']//p[6]//text()").get().strip()
        item['Link']='http://www.cddfct.com/'
        # location=response.xpath("//div[@class='copyright']/p[3]/text()[1]").get().strip().split("网",1)
        item['Location']='四川省成都市青羊区青华路37号'
        item['telephone']=''
        # response.xpath("//ul[@class='co']//p[12]//text()").get().strip()
        yield item