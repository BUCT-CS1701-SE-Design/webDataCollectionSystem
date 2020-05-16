# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection52Spider(scrapy.Spider):
    name = 'collection52'
    allowed_domains = ['wzmuseum.cn']
    start_urls = ['http://www.wzmuseum.cn/Col/Col5/Index.aspx']
    page = 1
    base_url = 'http://www.wzmuseum.cn/Col/Col5/Index_{}.aspx'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 52
        li_list = response.xpath("//ul[@class='jpul']/li")
        for li in li_list:
            item["collectionImage"] = 'http://www.wzmuseum.cn' + li.xpath(".//img/@src").extract_first().strip()
            item["collectionName"] = li.xpath(".//span/text()").extract_first().strip()
            url = li.xpath(".//a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

        # 完成每页之后开始下一页
        if self.page <= 1:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = '暂无介绍'
        item["collectionIntroduction"] = content
        yield item
