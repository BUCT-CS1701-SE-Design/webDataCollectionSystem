# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection51Spider(scrapy.Spider):
    name = 'collection51'
    allowed_domains = ['zhejiangmuseum.com']
    start_urls = ['http://www.zhejiangmuseum.com/zjbwg/collection/treasure.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 51
        li_list = response.xpath("//ul[@class='treasure']/li")
        for li in li_list:
            item["collectionImage"] = 'http://www.zhejiangmuseum.com' + li.xpath(".//img/@src").extract_first().strip()
            item["collectionName"] = li.xpath(".//p/text()").extract_first().strip()
            url = 'http://www.zhejiangmuseum.com/zjbwg/collection/' + li.xpath(".//a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//div[@class='jianjie']/p/span/text()|//div[@id='right_']/p/text()").extract()
        content = "\n".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
