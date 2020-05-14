# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }


class Museum63Spider(scrapy.Spider):
    name = 'museum63'
    allowed_domains = ['crt.com.cn']
    start_urls = ['http://www.crt.com.cn/mx/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=63
        item["museumName"]='中央苏区（闽西）历史博物馆'
        item["Location"]='福建省龙岩市北环西路51号'
        item["telephone"]='0597——2291479'
        item["Link"]='http://www.crt.com.cn/mx/'
        item["opentime"]='开放时间：星期二到星期日上午8：15到11：45，下午2：15到5：15，夏季：上午不变，下午3：00到5：45，实行免费开放;闭馆时间：每星期一'
        item["introduction"]='中央苏区（闽西）历史博物馆位于龙岩市新罗区北环西路51号，是一座全面反映闽西革命史、重点凸显中央苏区（闽西）历史的综合性革命博物馆。1981年在谭震林等老一辈无产阶级革命家生前提议下始建，1986年建成，1989年正式对外开放。2009年重新进行陈列改版和周边环境改造，2017年1月获评国家一级博物馆。目前占地面积30亩、建筑面积7000多平米、展厅面积5000多平米，馆藏文物近两万件，主要有《红色闽西》基本陈列和《闽西红土名人》《中央苏区·福建》等专题陈列。'
        yield item
