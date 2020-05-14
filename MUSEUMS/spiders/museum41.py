# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum41Spider(scrapy.Spider):
    name = 'museum41'
    allowed_domains = ['zgyd1921.com']
    start_urls = ['http://www.zgyd1921.com/zgyd/node3/n5/n6/ulai19.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 41
        item["museumName"] = '中国共产党第一次全国代表大会会址纪念馆'
        item["Location"] = '上海市黄浦区黄陂南路374号'
        item["Link"] = 'http://www.zgyd1921.com'
        item["opentime"] = '周二至周日（周一闭馆） 9:00-11:30（11:00停止入场） 13:00-16:30（16:00停止入场）'
        item["telephone"] = '021-53832171'
        content = response.xpath(
            "//div[@class='grey14 lh30']/p/text()").extract_first()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
