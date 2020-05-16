# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition37Spider(scrapy.Spider):
    name = 'exhibition37'
    allowed_domains = ['hljmuseum.com']
    start_urls = [
        'http://www.hljmuseum.com/clzl/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 37
        a = response.xpath("//div[@class='kuang'][position()<4]")
        li_list = a.xpath(
            "./div[@class='wxd-part fl']/div[@class='wxd-li']/ul/div[@class='wxd-li']/ul/li|./div[@class='wxd-part rl']/div[@class='wxd-li']/ul/div[@class='wxd-li']/ul/li")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath(
                "./a/text()").extract_first().strip()
            url = 'http://www.hljmuseum.com' + \
                li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                # meta={'item': copy.deepcopy(item)}  # 传递参数

                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["exhibition_picture"] = 'http://www.hljmuseum.com' + \
            response.xpath("//img/@src").extract_first().strip()
        content = response.xpath(
            "//div[@class='duanluo']/p/span/text()").extract()
        content = content[:3]
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
