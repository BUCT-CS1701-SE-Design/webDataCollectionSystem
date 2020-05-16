# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection37Spider(scrapy.Spider):
    name = 'collection37'
    allowed_domains = ['hljmuseum.com']
    start_urls = [
        'http://www.hljmuseum.com/cpgz/cpxs/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 37
        a = response.xpath("//div[@class='kuang'][position()<4]")
        li_list = a.xpath(
            "./div[@class='wxd-part fl']/div[@class='wxd-li']/ul/div[@class='wxd-li']/ul/li|./div[@class='wxd-part rl']/div[@class='wxd-li']/ul/div[@class='wxd-li']/ul/li")
        for li in li_list:
            item["collectionName"] = li.xpath(
                "./a/text()").extract_first().strip()
            url = 'http://www.hljmuseum.com' + \
                li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["collectionImage"] = 'http://www.hljmuseum.com' + \
            response.xpath("//img/@src").extract_first().strip()
        content = response.xpath(
            "//div[@class='duanluo']//span/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
