import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition104Spider(scrapy.Spider):
    name = 'exhibition104'
    allowed_domains = ['scmuseum.cn']
    start_urls = ['http://www.scmuseum.cn/list-1655.html']  
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=104
        a=1
        url1=response.xpath("//ul[@class='menu-sidebar']/li//@href").getall()
        for url in url1:
            if a==2 or a==4:
                continue
            a+=1
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        url1=response.xpath("//section[@id='zhanlan-left']/div[@class='zhanlanlist']//@href").getall()
        for url in url1:
            yield scrapy.Request(url,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//h1[@class='sbp-title']/text()").get().strip()
        introduce=response.xpath("//div[@id='MyContent']/p//text()").getall()
        item['exhibitionIntroduction']="".join(introduce).strip()
        item['exhibition_picture']='http://www.scmuseum.cn/'+response.xpath("//div[@id='MyContent']/p//@src").get()
        yield item 