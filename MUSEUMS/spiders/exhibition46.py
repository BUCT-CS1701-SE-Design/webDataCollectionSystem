# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition46Spider(scrapy.Spider):
    name = 'exhibition46'
    allowed_domains = ['ntmuseum.com']
    start_urls = [
        'http://www.ntmuseum.com/colunm3/col3/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 46
        li_list = response.xpath("//ul[@class='pic']/li")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath(".//span/text()").extract_first().strip()
            item["exhibition_picture"] = li.xpath(".//img/@src").extract_first().strip()
            url = li.xpath(".//a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//li[@class='list_all']/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
