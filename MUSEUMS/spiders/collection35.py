# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection35Spider(scrapy.Spider):
    name = 'collection35'
    allowed_domains = ['wangjinxi.org.cn']
    start_urls = ['http://www.wangjinxi.org.cn/plist.asp?id=17']
    page = 1
    base_url = 'http://www.wangjinxi.org.cn/plist.asp?id=17&page={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 35
        li_list = response.xpath("//div[@class='f2']")
        for li in li_list:
            item["collectionImage"] = 'http://www.wangjinxi.org.cn' + li.xpath( ".//img/@src").extract_first()
            item["collectionName"] = li.xpath(".//span/text()").extract_first()
            url = 'http://www.wangjinxi.org.cn/' + li.xpath(".//a/@href").extract_first().strip()

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

        content = response.xpath("//div[@id='zoom']/p/text()").extract()
        content = "\n".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
