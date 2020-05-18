import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition91Spider(scrapy.Spider):
    name = 'exhibition91'
    allowed_domains = ['gznywmuseum.org']
    start_urls = ['https://www.gznywmuseum.org/zlgg/index.jhtml'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=91
        a=1
        url1=response.xpath("///div[@id='zldtlist']/div//@href").getall()
        for url in url1:
            url='https://www.gznywmuseum.org/'+url
            if a>5:
                break
            a+=1
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//p[@class='nbsp-sp-detail-title']/text()").get().strip()
        ex=response.xpath("//div[@class='nbsp-sp-detail-view-middle']/p//text()").getall()
        item['exhibitionIntroduction']="".join(ex).strip()
        item['exhibition_picture']='http://www.eywsqsfbwg.com/'+response.xpath("//div[@class='nbsp-sp-detail-view-middle']/p//@src").get()
        yield item   