# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item

class Collection38Spider(scrapy.Spider):
    name = 'collection38'
    allowed_domains = ['dqsbwg.com']
    start_urls = ['http://www.dqsbwg.com/cp.asp?classid=3']
    page = 1
    base_url = 'http://www.dqsbwg.com/cp.asp?classid=3&xclassid=&bp={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item=collection75Item()
        item["museumID"]=38
        li_list = response.xpath("//td[@class='ns']/table/tr[position()=2]/td/table/tr/td/table/tr")
        for a in li_list:
            b = a.xpath("./td[position()=2]")
            for li in b:
                image_url = li.xpath(
                    ".//img/@src").extract_first().strip()
                item["collectionImage"] = 'http://www.dqsbwg.com' + \
                    image_url[2:]
                item["collectionName"] = li.xpath(
                    ".//font/text()").extract_first()
                item["collectionIntroduction"] = '暂无介绍'
                yield item

                # 完成每页之后开始下一页
                if self.page <= 4:
                    self.page += 1
                    new_url = self.base_url.format(self.page)
                    yield scrapy.Request(url=new_url, callback=self.parse)


