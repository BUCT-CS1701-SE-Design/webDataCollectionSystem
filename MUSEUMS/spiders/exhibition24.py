import scrapy
from MUSEUMS.items import exhibition75Item 

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition24'
    allowed_domains = ['www.nmgbwy.com']
    start_urls = ['http://www.nmgbwy.com/zldt/1558.jhtml?contentId=1558']
    def parse(self, response):
        li_list=response.xpath("//div/ul[@class='photos']/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=24
            item["exhibitionTheme"]=li.xpath("./div[@class='right']/h1/text()").extract_first().replace(" ","")
            item["exhibition_picture"]=li.xpath("./div[@class='left']/img/@src").extract_first()
            item["exhibitionIntroduction"]=li.xpath("./div[@class='right']/p/text()").extract_first()
            yield item
       
       

        










