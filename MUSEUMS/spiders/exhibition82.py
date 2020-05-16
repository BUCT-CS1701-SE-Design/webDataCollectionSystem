import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition82Spider(scrapy.Spider):
    name = 'exhibition82'
    allowed_domains = ['jzmsm.org']
    start_urls = ['http://www.jzmsm.org/yk/zhanlan/']
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=80
        url1=response.xpath("//div[@class='jyzn_l']/ul//@href").getall()
        for url in url1:
            url='http://www.jzmsm.org'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        url2=response.xpath("//div[@class='gbxs']//a/@href").getall()
        a=0
        for url in url2:
            url='http://www.jzmsm.org'+url
            a+=1
            if a>5:
                break
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//div[@class='content']//text()").get()
        exhibitionIntroduction= response.xpath("//div[@class='content']/p/span[1]/text()").getall()
        item['exhibitionIntroduction']="".join(exhibitionIntroduction).strip()
        picture=response.xpath("//div[@class='yknr_mav']/div[3]/p/img/@src").getall()
        temp=[]
        for pic in picture:
            pic='http://www.jzmsm.org'+str(pic)+'\t'
            temp+=pic
        item['exhibition_picture']="".join(temp)
        yield item 