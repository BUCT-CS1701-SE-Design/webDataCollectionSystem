# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item


class Collection29Spider(scrapy.Spider):
    name = 'collection29'
    allowed_domains = ['sypm.org.cn']
    start_urls = [
        'http://www.sypm.org.cn/products_list3/&pmcId=77&comp_stats=comp-FrontProductsCategory_show01-ycjd.html']
    page = 1
    base_url = 'http://www.sypm.org.cn/products_list3/&pmcId=77&comp_stats=comp-FrontProductsCategory_show01-ycjd&pageNo_FrontProducts_list01-0042={}&pageSize_FrontProducts_list01-0042=20.html'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 29
        li_list = response.xpath("//ul[@class='mainul productlist-02']//li[@class='content column-num4']")
        for li in li_list:
            image_url = li.xpath("./div[@class='pic-module']/div[@class='pic']/a/img/@src").extract_first().strip()
            item["collectionImage"] = 'http://www.sypm.org.cn' + image_url
            url = 'http://www.sypm.org.cn' + \
                li.xpath("./div[@class='pic-module']/div[@class='pic']/a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

        # 完成每页之后开始下一页
        if self.page <= 1:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        name = response.xpath("//li[@class='name1']/text()").extract()
        name = "".join(name).strip()
        item["collectionName"] = name
        content = response.xpath(
            "//div[@class='FrontProducts_detail02-0012_htmlbreak']/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
