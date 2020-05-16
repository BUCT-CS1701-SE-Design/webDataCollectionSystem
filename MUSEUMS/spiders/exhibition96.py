import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition96Spider(scrapy.Spider):
    name = 'exhibition96'
    allowed_domains = ['gxmuseum.cn']
    start_urls = ['http://www.gxmuseum.cn/a/exhibition/index.html']
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=96
        a=0
        url1=response.xpath("//ul[@class='d3']/li/a[1]/@href").getall()
        for url in url1:
            a+=1
            if a>3:
                break
            url='http://www.gxmuseum.cn'+url
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        lilist=response.xpath("//div[@class='dp_list']")
        for li in lilist:
            item=response.meta["item"]
            # exhibitionTime=
            item['exhibitionTheme']=li.xpath(".//p[1]//@title").get().strip()
            item['exhibitionIntroduction']="".join(li.xpath(".//p[3]//text()").getall()).strip()
            item['exhibition_picture']='http://www.gxmuseum.cn'+li.xpath("./div[1]//img/@src").get()
            yield item