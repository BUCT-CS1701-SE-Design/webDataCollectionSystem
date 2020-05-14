# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection46Spider(scrapy.Spider):
    name = 'collection46'
    allowed_domains = ['ntmuseum.com']
    start_urls = ['http://www.ntmuseum.com/colunm2/col1/list_17_1.html']
    page = 1
    base_url = 'http://www.ntmuseum.com/colunm2/col1/list_17_{}.html'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 46
        li_list = response.xpath("//ul[@class='pic']/li")
        for li in li_list:
            item["collectionImage"] = li.xpath(".//img/@src").extract_first().strip()
            item["collectionName"] = li.xpath(".//span/text()").extract_first().strip()
            url = li.xpath(".//a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

        # 完成每页之后开始下一页
        if self.page <= 4:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//li[@class='list_all']//div/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
