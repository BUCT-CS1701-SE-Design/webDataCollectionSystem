import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition84Spider(scrapy.Spider):
    name = 'exhibition84'
    allowed_domains = ['1911museum.com']
    start_urls = ['http://www.1911museum.com/Exhibition/List/jbcl'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=84
        url2=response.xpath("//ul[@class='collectlist basicexhlist']/li//@href").getall()
        for url in url2:
                url='http://www.1911museum.com'+url
                yield scrapy.Request(url,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//div[@class='title']/text()").get().strip()
        item['exhibition_picture']=response.xpath("//div[@class='cont']/p/img/@src").get()
        exhibitionIntroduction=response.xpath("//div[@class='cont']//text()").getall()
        item['exhibitionIntroduction']="".join(exhibitionIntroduction).strip()
        yield item  