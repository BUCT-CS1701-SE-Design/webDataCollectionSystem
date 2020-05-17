# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum29Spider(scrapy.Spider):
    name = 'museum29'
    allowed_domains = ['sypm.org.cn']
    start_urls = ['http://www.sypm.org.cn/news_detail/newsId=329.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 29
        item["museumName"] = '沈阳故宫博物院'
        item["Location"] = '中国辽宁省沈阳市沈河区沈阳路171号'
        item["Link"] = 'http://www.sypm.org.cn'
        opentime = response.xpath(
            "//div[@class='describe htmledit']/p/text()").extract()
        opentime = "".join(opentime).strip()
        item["opentime"] = opentime
        item["telephone"] = '024-24843001'
        url = 'http://www.sypm.org.cn/comcontent_detail.html'
        # 处理详情页
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={'item': copy.deepcopy(item)}  # 传递参数
        )

    def parse_detail(self, response):
        item = response.meta["item"]
        content = response.xpath(
            "////div[@class='FrontComContent_detail01-001_htmlbreak']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
