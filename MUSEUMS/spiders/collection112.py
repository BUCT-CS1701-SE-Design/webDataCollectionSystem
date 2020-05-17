# -*- coding: utf-8 -*-
import scrapy
import re
import sys
sys.path.append('..')
from items import collection75Item

class Collection112Spider(scrapy.Spider):
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.Collection75Pipeline': 4, }
    }
    name = 'collection112'
    allowed_domains = ['cmnh.org.cn']
    start_urls = ['https://www.cmnh.org.cn/list/?26.html']

    def parse(self, response):
        li_list = response.xpath("//div[2]/div[3]//div[2]/div[1]/ul/li")
        for li in li_list:
            item = collection75Item()
            item["museumID"] = 112
            item["collectionName"] = li.xpath("./div/div[2]/a/h6").extract_first()
            item["collectionImage"] ="https://www.cmnh.org.cn"+li.xpath("./p/a/img/@src").extract_first()
            url ='https://www.cmnh.org.cn'+li.xpath("./p/a/@href").extract_first()
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        p_list = response.xpath("//div[2]/div[3]//div[2]//span")
        content = ""
        for p in p_list:
            x = p.xpath("./text()").extract_first()
            if x != None:
                content += x
                # break
        # print(content)
        item["collectionIntroduction"] = content
        yield item

