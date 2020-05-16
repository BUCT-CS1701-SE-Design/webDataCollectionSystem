# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum35Spider(scrapy.Spider):
    name = 'museum35'
    allowed_domains = ['wangjinxi.org.cn']
    start_urls = ['http://www.wangjinxi.org.cn/page.asp?id=2']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 35
        item["museumName"] = '大庆铁人王进喜纪念馆'
        item["Location"] = '大庆市让胡路区中原路3号'
        item["Link"] = 'http://www.wangjinxi.org.cn'
        item["opentime"] = '每周二至周日08:00-16:00 下午16:00停止入场，节假日、每逢周一闭馆'
        item["telephone"] = '0459-5935100'
        content = response.xpath("//div[@class='page_info_content']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        print(item)
        yield item
