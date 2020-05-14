# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum33Spider(scrapy.Spider):
    name = 'museum33'
    allowed_domains = ['wmhg.com.cn']
    start_urls = ['https://www.wmhg.com.cn/aboutus.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 33
        item["museumName"] = '伪满皇宫博物院'
        item["Location"] = '吉林省长春市陕西路与光复北路交汇'
        item["Link"] = 'https://www.wmhg.com.cn'
        item["opentime"] = '夏季时间05月01日至9月30日: 8:30售票进馆 16:20停止售票 17:20闭馆  冬季时间10月1日至翌年4月30日: 8:30售票进馆 15:40停止售票 16:50闭馆'
        item["telephone"] = '0431-82866611'
        content = response.xpath(
            "//div[@class='section1']//div[@class='p']/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
