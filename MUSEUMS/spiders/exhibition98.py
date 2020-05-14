import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition98Spider(scrapy.Spider):
    name = 'exhibition98'
    allowed_domains = ['hainanmuseum.org']
    start_urls = ['http://www.hainanmuseum.org/zlhd/?tag_id=1','http://www.hainanmuseum.org/zlhd/?tag_id=2'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=98
        a=0
        url1=response.xpath("//ul[@class='new-body']/li//@href").getall()
        for url in url1:
            a+=1
            url='http://www.hainanmuseum.org/'+url
            if a>6:
                break
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//div[@class='title']/text()").get().strip()
        item['exhibitionIntroduction']="".join(response.xpath("//div[@class='article_cont']/p//text()").getall()).strip().replace('\r\n','')
        picture=response.xpath("//div[@class='article_cont']//@src").getall()
        photo=''
        for pic in picture:
            photo+='http://www.hainanmuseum.org'+pic+'\t'
        item['exhibition_picture']=photo
        yield item 