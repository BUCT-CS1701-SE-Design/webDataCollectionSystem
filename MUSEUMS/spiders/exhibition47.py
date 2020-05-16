# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition47Spider(scrapy.Spider):
    name = 'exhibition47'
    allowed_domains = ['szmuseum.com']
    start_urls = ['http://www.szmuseum.com/Exhibition/Index']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 47
        li_list = response.xpath("//div[@class='exjblb']/ul/li")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath(".//h1/text()").extract_first().strip()
            item["exhibition_picture"] = li.xpath(".//img/@src").extract_first().strip()
            url = 'http://www.szmuseum.com' + li.xpath(".//a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//div[@class='divContent']//p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
