import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition90Spider(scrapy.Spider):
    name = 'exhibition90'
    allowed_domains = ['gdmuseum.com']
    start_urls = ['http://www.gdmuseum.com/gdmuseum/_300730/index.html'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=90
        url1=[]
        url1+=response.xpath("//div[@class='column_list']/a[1]/@href").getall()
        url1+=response.xpath("//div[@class='column_list']/a[2]/@href").getall()
        for url in url1:
            url='http://www.gdmuseum.com/'+url
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        url2=response.xpath("//div[@class='product_w']/div//@href").getall()
        for ur in url2:
            ur='http://www.gdmuseum.com/'+ur
            yield scrapy.Request(ur,callback=self.Info,meta={"item":item})
    def Info(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//div[@class='jianjie_head']/div[1]/text()").get().strip()
        ex=response.xpath("//div[@class='zl_cont']/p/text()").get().strip()
        item['exhibitionIntroduction']="".join(ex).strip()
        item['exhibition_picture']='http://www.gdmuseum.com/'+response.xpath("//div[@class='datu_cont']/img/@src").get()
        yield item 