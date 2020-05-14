import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition93Spider(scrapy.Spider):
    name = 'exhibition93'
    allowed_domains = ['shenzhenmuseum.com']
    start_urls = ['https://www.shenzhenmuseum.com/exhibition/index#permanent'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=93
        Li_list=response.xpath("//ul[@class='clear']/li[@class='item']")
        for li in Li_list:
            # exhibitionTime=
            item['exhibitionTheme']=li.xpath(".//h3//text()").get().strip()
            item['exhibitionIntroduction']="".join(li.xpath(".//p//text()").getall()).strip()
            item['exhibition_picture']=li.xpath(".//div/img/@src").get()
            yield item