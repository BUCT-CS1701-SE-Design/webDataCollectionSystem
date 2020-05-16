# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection48Spider(scrapy.Spider):
    name = 'collection48'
    allowed_domains = ['yzmuseum.com']
    start_urls = ['https://www.yzmuseum.com/website/treasure/list.php']
    page = 1
    base_url = 'https://www.yzmuseum.com/website/treasure/list.php?page={}&type=1'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 48
        li_list = response.xpath("//div[@class='treasure_item']")
        for li in li_list:
            image_url = li.xpath(".//div[@class='pic_area']/@style").extract_first().strip()
            item["collectionImage"] = 'https://www.yzmuseum.com' + image_url[22:-1]
            item["collectionName"] = li.xpath(".//p/text()").extract_first().strip()
            url = 'https://www.yzmuseum.com/' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

        # 完成每页之后开始下一页
        if self.page <= 4:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//div[@id='content_text']/p/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
