import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition89Spider(scrapy.Spider):
    name = 'exhibition89'
    allowed_domains = ['chinajiandu.cn']
    start_urls = ['http://www.chinajiandu.cn/Exhibition/Index'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=89
        url1=response.xpath("//div[@class='allcenter']/ul/li[4]//li//@href").getall()
        for url in url1:
            url='http://www.chinajiandu.cn'+url
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        some=response.xpath("//div[@class='innercont']//ul/li")
        for link in some:
            item=response.meta["item"]
            # exhibitionTime=
            item['exhibitionTheme']=link.xpath(".//a/h3/text()").get().strip()
            exhibitionIntroduction=link.xpath("./div//text()").getall()
            item['exhibitionIntroduction']="".join(exhibitionIntroduction).strip()
            item['exhibition_picture']=link.xpath("./a/div/img/@src").get()
            yield item