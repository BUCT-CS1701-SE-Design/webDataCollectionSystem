# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection41Spider(scrapy.Spider):
    name = 'collection41'
    allowed_domains = ['zgyd1921.com']
    start_urls = [
        'http://www.zgyd1921.com/zgyd/node3/n17/n18/index.html']
    page = 0
    base_url = 'http://www.zgyd1921.com/zgyd/node3/n17/n18/index{}.html'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 41
        li_list = response.xpath("//ul[@class='piclist2']/li")
        for li in li_list:
            item["collectionImage"] = 'http://www.zgyd1921.com' + li.xpath("./a/img/@src").extract_first().strip()
            item["collectionName"] = li.xpath("./p/a/text()").extract_first().strip()
            url = 'http://www.zgyd1921.com' + li.xpath("./a/@href").extract_first().strip()

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

        contentraw = response.xpath("//div[@class='grey14 lh30']/p/text()").extract()
        content = "".join(contentraw[-1]).strip()
        if('简介' not in content):
            content = "".join(contentraw[-2]).strip()
        item["collectionIntroduction"] = content
        yield item
