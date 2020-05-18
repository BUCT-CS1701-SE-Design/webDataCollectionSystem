# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection50Spider(scrapy.Spider):
    name = 'collection50'
    allowed_domains = ['njmuseumadmin.com']
    start_urls = ['http://www.njmuseumadmin.com/Antique/lists']
    page = 1
    base_url = 'http://www.njmuseumadmin.com/Antique/lists/p/{}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 50
        li_list = response.xpath("//div[@class='Object_listcon']/ul/li")
        for li in li_list:
            item["collectionImage"] = 'http://www.njmuseumadmin.com' + li.xpath(".//img/@src").extract_first().strip()
            item["collectionName"] = li.xpath(".//span/text()").extract_first().strip()
            url = 'http://www.njmuseumadmin.com' + li.xpath(".//a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

        # 完成每页之后开始下一页
        if self.page <= 3:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//div[@class='gundongtiao']/p/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
