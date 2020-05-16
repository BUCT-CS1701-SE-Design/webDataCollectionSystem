# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection45Spider(scrapy.Spider):
    name = 'collection45'
    allowed_domains = ['19371213.com.cn']
    start_urls = [
        'http://www.19371213.com.cn/collection/featured/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 45
        li_list = response.xpath("//div[@id='Data_con']/div")
        for li in li_list:
            image_url = li.xpath(".//img/@src").extract_first().strip()
            item["collectionImage"] = 'http://www.19371213.com.cn/collection' + image_url[2:]
            item["collectionName"] = li.xpath(".//h3/a/text()").extract_first().strip()
            u = li.xpath(".//a/@href").extract_first().strip()
            url = 'http://www.19371213.com.cn/collection' + u[2:]

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//p[@class='rtejustify rteindent2']/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
