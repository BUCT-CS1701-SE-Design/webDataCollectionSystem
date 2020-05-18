import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition80Spider(scrapy.Spider):
    name = 'exhibition80'
    allowed_domains = ['eywsqsfbwg.com']
    start_urls = ['http://www.eywsqsfbwg.com/index.php?m=content&c=index&a=lists&catid=10']
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=80
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//div[@id='D1pic1']/div/a/@title").get().strip()
        item['exhibitionIntroduction']=response.xpath("//div[@class='xlzl_intro fr']/text()").get().strip()
        item['exhibition_picture']='http://www.eywsqsfbwg.com/'+response.xpath("//div[@id='D1pic1']/div/a/img/@src").get()
        yield item      
