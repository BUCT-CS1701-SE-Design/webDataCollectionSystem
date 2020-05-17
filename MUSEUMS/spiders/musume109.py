# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume109Spider(scrapy.Spider):
    name = 'musume109'
    allowed_domains = ['ynnmuseum.com']
    start_urls = ['http://www.ynnmuseum.com/lianxi.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumsPipeline': 1, }
    }

    def parse(self, response):
        item = MuseumsItem()
        item["museumID"] = 109
        item["museumName"] = '云南名族博物馆'
        item["Location"] = response.xpath('normalize-space(/html//div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/p[1])').extract_first()
        item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"] = 'http://www.ynnmuseum.com/main.html'
        item["opentime"] = '开放时间：周二至周日上午9:00——下午4:30（周一闭馆）'
        item["telephone"] = response.xpath(
            'normalize-space(/html//div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/p[3])').extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')

        url = 'http://www.ynnmuseum.com/abouts.html'
        # 处理详情页

        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item": item}  # 传递参数
        )

    def parse_detail(self, response):
        item = response.meta["item"]
        item["introduction"] = response.xpath(
            'normalize-space(/html//div/div/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/p[2]/text())').extract_first()
        #item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        #item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        # print(item)
        yield item
