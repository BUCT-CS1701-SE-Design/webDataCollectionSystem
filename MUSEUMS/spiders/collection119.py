# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from MUSEUMS.items import collection75Item

class Collection119Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection119'
    allowed_domains = ['zgshm.cn']
    base_url='https://bpmuseum.com/index.php?m=content&c=index&a=lists&catid='
    offset = 19
    start_urls = [base_url+str(offset)]

    def parse(self, response):
        li_list = response.xpath("//div[@class='con12']")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 119
            item["collectionName"] = li.xpath(".//h3/a/text()").extract_first()
            item["collectionImage"] ="http://www.zgshm.cn/"+li.xpath(".//img/@src").extract_first()
            item["collectionIntroduction"]=' '
            yield item

        if self.offset <21:
            self.offset+=1
            url=self.base_url+str(self.offset)
            yield scrapy.Request(
                url,
                callback=self.parse,
                meta={"item": item}
            )
        if self.offset == 21:
            self.offset =40
            url = self.base_url + str(self.offset)
            yield scrapy.Request(
                url,
                callback=self.parse,
                meta={"item": item}
            )


