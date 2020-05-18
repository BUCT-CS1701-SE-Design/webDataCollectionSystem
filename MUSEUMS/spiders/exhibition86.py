import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition86Spider(scrapy.Spider):
    name = 'exhibition86'
    allowed_domains = ['hnmuseum.com']
    start_urls = ['http://www.hnmuseum.com/zh-hans/content/%E5%BD%93%E5%89%8D%E5%B1%95%E8%A7%88%EF%BC%8D%E5%9F%BA%E6%9C%AC%E9%99%88%E5%88%97'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=86
        url1=response.xpath("//div[@class='view-content']//h3//@href").getall()
        for url in url1:
            url='http://www.hnmuseum.com/'+url
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//div[@class='field-items']//h3/text()").get()
        exhibitionIntroduction= response.xpath("//div[@id='node-850']//div[@class='right']/p/text()").getall()
        item['exhibitionIntroduction']="".join(exhibitionIntroduction).strip()
        pic=response.xpath("//div[@class='zt_topcontent container']//img/@src").getall()
        item['exhibition_picture']="".join(pic)
        yield item 