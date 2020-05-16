# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition50Spider(scrapy.Spider):
    name = 'exhibition50'
    allowed_domains = ['njmuseumadmin.com']
    start_urls = ['http://www.njmuseumadmin.com/Exhibit/index/id/14']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 50
        li_list = response.xpath("//div[@class='basic_downcon']/a")
        for li in li_list:
            item["exhibition_picture"] = 'http://www.njmuseumadmin.com' + li.xpath(".//img/@src").extract_first().strip()
            url = 'http://www.njmuseumadmin.com' + li.xpath("./@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["exhibitionTheme"] = response.xpath("//div[@class='basicxx_downtitle']/span/text()").extract_first().strip()
        content = response.xpath("//div[@class='basicxx_p']/p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
