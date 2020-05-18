# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection32Spider(scrapy.Spider):
    name = 'collection32'
    allowed_domains = ['jlmuseum.org']
    start_urls = [
        'http://www.jlmuseum.org/collection/']
    page = 1
    base_url = 'http://www.jlmuseum.org/collection/{}.html'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 32
        li_list = response.xpath("//div[@class='list-pics']/ul//li")
        for li in li_list:
            image_url = li.xpath("./div[@class='thumb']/a/img/@src").extract_first().strip()
            item["collectionImage"] = 'http://www.jlmuseum.org' + image_url
            item["collectionName"] = li.xpath("./div[@class='info']/a/text()").extract_first().strip()
            url = 'http://www.jlmuseum.org' + li.xpath("./div[@class='thumb']/a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

        # 完成每页之后开始下一页
        if self.page <= 2:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath(
             "//div[@class='content']/div[@class='pics-cont']/p/font/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
