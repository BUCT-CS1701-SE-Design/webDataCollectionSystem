import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition97Spider(scrapy.Spider):
    name = 'exhibition97'
    allowed_domains = ['amgx.org']
    start_urls = ['http://www.amgx.org/exhibimore-483.html'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=97
        a=0
        url1=response.xpath("//div[@class='mbinnerla']/ul/li/a/@href").getall()
        for url in url1:
            a+=1
            if a>1 and a<=4:
                url='http://www.amgx.org/'+url
                yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
            else:
                continue
    def Intro(self,response):
        divlist=response.xpath("//div[@class='lzhg']")
        for li in divlist:
            item=response.meta["item"]
            # exhibitionTime=
            item['exhibitionTheme']="".join(li.xpath(".//div[1]//text()").getall()).strip()
            item['exhibitionIntroduction']=li.xpath(".//p/text()").get().strip()
            item['exhibition_picture']='http://www.amgx.org'+li.xpath(".//img/@src").get()
            yield item