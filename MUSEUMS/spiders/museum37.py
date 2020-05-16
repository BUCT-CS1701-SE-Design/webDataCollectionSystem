# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum37Spider(scrapy.Spider):
    name = 'museum37'
    allowed_domains = ['hljmuseum.com']
    start_urls = ['http://www.hljmuseum.com/system/200910/101021.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 37
        item["museumName"] = '黑龙江省博物馆'
        item["Location"] = '南岗区红军街64号'
        item["Link"] = 'http://www.hljmuseum.com'
        item["opentime"] = '周二至周日；9:00～16:30（15:30停止发票）'
        item["telephone"] = '0451-53644151'
        content = response.xpath(
            "//span[@style='font-size:18px;']/p/span/text()").extract()
        content = content[:2]
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
