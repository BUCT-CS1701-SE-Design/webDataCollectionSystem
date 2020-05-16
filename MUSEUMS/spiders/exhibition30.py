# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition30Spider(scrapy.Spider):
    name = 'exhibition30'
    allowed_domains = ['dlmodernmuseum.com']
    start_urls = [
        'https://www.dlmodernmuseum.com/exhibition/display/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 30
        li_list = response.xpath("//div[@class='showlist contrightlist']/ul//li")
        for li in li_list:
            item["exhibition_picture"] = li.xpath("./a/div[@class='showimg1 w340 h510']/img/@src").extract_first().strip()
            url = li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}  # 传递参数
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["exhibitionTheme"] = response.xpath("//div[@class='showlist contrightlist']/h2[@class='tacenter']/text()").extract_first().strip()
        content = response.xpath(
            "//div[@class='showlist contrightlist']/p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
