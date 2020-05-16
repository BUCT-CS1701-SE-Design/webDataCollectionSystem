# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition48Spider(scrapy.Spider):
    name = 'exhibition48'
    allowed_domains = ['yzmuseum.com']
    start_urls = ['https://www.yzmuseum.com/website/exhibition/basic.php?id=23']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 48
        image_url = response.xpath("//div[@id='img1']/@style").extract_first().strip()
        item["exhibition_picture"] = 'https://www.yzmuseum.com' + image_url[22:-1]
        item["exhibitionTheme"] = response.xpath("//div[@class='content_head_item  onfocus']/a/text()").extract_first().strip()
        content = response.xpath("//div[@class='content_text']/p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        li_list = response.xpath("//div[@class='content_head_item ']")
        for li in li_list:
            item = exhibition75Item()
            item["museumID"] = 48
            item["exhibitionTheme"] = li.xpath("./a/text()").extract_first().strip()
            url = 'https://www.yzmuseum.com/' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        image_url = response.xpath("//div[@id='img1']/@style").extract_first().strip()
        item["exhibition_picture"] = 'https://www.yzmuseum.com' + image_url[22:-1]
        content = response.xpath("//div[@class='content_text']/p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
