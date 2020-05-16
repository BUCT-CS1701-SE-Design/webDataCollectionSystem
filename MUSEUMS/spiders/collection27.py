# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection27Spider(scrapy.Spider):
    name = 'collection27'
    allowed_domains = ['918museum.org.cn']
    start_urls = [
        'http://www.918museum.org.cn/index.php/article/listarticle/pid/126/rel/thumb/sidebar/sidebar']
    page = 1
    base_url = 'http://www.918museum.org.cn/index.php/article/listarticle/pid/126/rel/thumb/sidebar/sidebar?currentPage={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 27
        li_list = response.xpath("//div[@class='article row ']/div")
        for li in li_list:
            image_url = li.xpath("./a/img/@src").extract_first().strip()
            item["collectionImage"] = 'http://www.918museum.org.cn' + image_url
            url = 'http://www.918museum.org.cn' + \
                li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}  # 传递参数
            )

        # 完成每页之后开始下一页
        if self.page <= 5:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath(
            "//div[@class='article box']/div[@class='article_content']/p/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        item["collectionName"] = response.xpath(
            "//div[@class='article_title']/text()").extract_first().strip()
        yield item
