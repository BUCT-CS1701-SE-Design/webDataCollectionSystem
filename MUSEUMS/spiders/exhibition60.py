# -*- coding: utf-8 -*-
import scrapy
import re 
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item


class Exhibition60Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }
    name = 'exhibition60'
    allowed_domains = ['gthyjng.com']
    start_urls = ['http://www.gthyjng.com/gqjs/']

    def parse(self, response):
        li_list=response.xpath("//div[@class='win_a']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=60
            item["exhibitionTheme"]=li.xpath("./a/p/text()").extract_first()
            url='http://www.gthyjng.com/gqjs/'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                    url,
                    callback=self.parse_detail,
                    meta={"item":item}
                )
    def parse_detail(self,response):
        item=response.meta["item"]
        if response.xpath("//div[@class='sub']/p/img/@oldsrc").extract_first() is not None:

            item["exhibition_picture"]='http://www.gthyjng.com/gqjs/gthyhz/'+response.xpath("//div[@class='sub']/p/img/@src").extract_first()
        else:
            item["exhibition_picture"]=''
        #item["exhibitionIntroduction"]=response.xpath("//div[@class='sub']/p[1]/font/text()").extract()
        tag=response.text
        item["exhibitionIntroduction"]=re.findall('<font size="3" style="font-family: Simsun; color: rgb(0,0,0); line-height: 24px">(.*?)<br />',str(tag))
        item["exhibitionTime"]=''
        #print(item)
        yield item
                #item["exhibition_picture"]=li.xpath("")
