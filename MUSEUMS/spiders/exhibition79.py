import scrapy
from MUSEUMS.items import exhibition75Item

class Exhibition79Spider(scrapy.Spider):
    name = 'exhibition79'
    allowed_domains = ['kfsbwg.com']
    start_urls = ['http://www.kfsbwg.com/html/zhanlan/']
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=79
        lurl=response.xpath('//*[@id="Map"]/area/@href').extract()
        for url in lurl:
            url='http://www.kfsbwg.com'+url
            yield scrapy.Request(url,callback=self.Others,meta={"item":item})

    def Others(self,response):
        li_list=response.xpath("//*[@id='list']/div/ul/li")
        
        for li in li_list:
            item=response.meta["item"]
            exhibitionTime=li.xpath('/p[2]/text()').get()
            item["exhibitionTime"]=exhibitionTime
            exhibitionTheme=li.xpath('./p[1]/text()').get()
            item["exhibitionTheme"]=exhibitionTheme
            exhibitionIntroduction=li.xpath("./p[4]/text()").get()
            item["exhibitionIntroduction"]=exhibitionIntroduction
            exhibition_picture=li.xpath("./div/a/img/@src").get()
            item["exhibition_picture"]=exhibition_picture
            yield item
