# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum27Spider(scrapy.Spider):
    name = 'museum27'
    allowed_domains = ['918museum.org.cn']
    start_urls = [
        'http://www.918museum.org.cn/index.php/article/listarticle/pid/171/rel/detail/sidebar/sidebar']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 27
        item["museumName"] = '“九·一八”历史博物馆'
        item["Location"] = '辽宁省沈阳市大东区望花南街46号'
        item["Link"] = 'http://www.918museum.org.cn'
        opentime = response.xpath(
            "//div[@class='article_content']/p[position()=3]/span/text()").extract()
        opentime = "".join(opentime).strip()
        item["opentime"] = opentime
        item["telephone"] = '024-88331017'
        url = 'http://www.918museum.org.cn/index.php/article/listarticle/pid/104/rel/detail/sidebar/sidebar'
        # 处理详情页
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item": item}  # 传递参数
        )

    def parse_detail(self, response):
        item = response.meta["item"]
        content = response.xpath(
            "//div[@class='article_content']/p/text()").extract()
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
