# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item


class Collection30Spider(scrapy.Spider):
    name = 'collection30'
    allowed_domains = ['dlmodernmuseum.com']
    start_urls = [
        'https://www.dlmodernmuseum.com/collection/']
    page = 1
    base_url = 'https://www.dlmodernmuseum.com/collection/{}.html'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 30
        li_list = response.xpath("//div[@class='showlist contrightlist']/ul//li")
        for li in li_list:
            image_url = li.xpath("./a/div[@class='showimg2']/img/@src").extract_first().strip()
            item["collectionImage"] = 'https://www.dlmodernmuseum.com' + image_url
            url = li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

        # 完成每页之后开始下一页
        if self.page <= 2:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["collectionName"] = response.xpath("//div[@class='showlist contrightlist']/h2[@class='tacenter']/text()").extract_first().strip()
        content = response.xpath(
             "//div[@class='showlist contrightlist']/p/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
