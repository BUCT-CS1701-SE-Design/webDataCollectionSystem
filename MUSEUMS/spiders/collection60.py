# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item


class Collection60Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }

    name = 'collection60'
    allowed_domains = ['gthyjng.com']
    start_urls = ['http://www.gthyjng.com/gcww/wwjs/tdgmsq/']

    def parse(self, response):
        li_list=response.xpath("//div[@class='news_r_img']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=60
            url='http://www.gthyjng.com/gcww/wwjs/tdgmsq/'+li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                    url,
                    callback=self.parse_detail,
                    meta={"item":item}
                )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["collectionName"]=response.xpath("//div[@class='xl_top']/h1/text()").extract_first()
        #response.xpath("//div[@class='xl_nr mar_t20']/div[@class='TRS_Editor']/div/a/@href").extract_first()
        if response.xpath("//div[@class='xl_nr mar_t20']/div[@class='TRS_Editor']/div/img/@oldsrc").extract_first() is not None:

            item["collectionImage"]='http://www.gthyjng.com/gcww/wwjs/tdgmsq/202004/'+response.xpath("//div[@class='xl_nr mar_t20']/div[@class='TRS_Editor']/div/img/@oldsrc").extract_first()
        else:
            item["collectionImage"]=''
        item["collectionIntroduction"]=''
        #print(item)
        yield item