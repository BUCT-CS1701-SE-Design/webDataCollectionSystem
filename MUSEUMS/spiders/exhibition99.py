import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition99Spider(scrapy.Spider):
    name = 'exhibition99'
    allowed_domains = ['zdm.cn']
    start_urls = ['http://www.zdm.cn/temporary.html'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=99
        url1=response.xpath("//div[@class='container']/a/@href").getall()
        for url in url1:
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//p[@class='title']/text()").get().strip()
        item['exhibitionIntroduction']="".join(response.xpath("//div[@class='textBox']//text()").getall()).strip()
        item['exhibition_picture']="".join(response.xpath("//div[@class='textBox']//@src").getall()).strip()
        yield item   