# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition40Spider(scrapy.Spider):
    name = 'exhibition40'
    allowed_domains = ['luxunmuseum.cn']
    start_urls = [
        'http://www.luxunmuseum.cn/lxcl/index.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 40
        li_list = response.xpath("//ul[@class='am-nav']/li[position()>1]")
        for li in li_list:
            url = 'http://www.luxunmuseum.cn' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["exhibition_picture"] = response.xpath("//div[@class='am-align-left']/a/img/@src").extract_first().strip()
        item["exhibitionTheme"] = response.xpath("//div[@class='am-align-left']/h3/text()").extract_first().strip()
        content = response.xpath("//div[@class='am-align-left']/text()").extract()
        content = "".join(content[3:]).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
