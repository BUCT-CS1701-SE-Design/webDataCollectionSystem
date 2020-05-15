# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置



class Museum64Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
    name = 'museum64'
    allowed_domains = ['jgsgmbwg.com']
    start_urls = ['http://www.jgsgmbwg.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=64
        item["museumName"]='井冈山革命博物馆'
        item["Location"]='江西省井冈山茨坪红军南路'
        item["telephone"]='0796-6552248/6555625'
        item["Link"]='http://www.jgsgmbwg.com/'
        item["opentime"]=''
        item["introduction"]=' 井冈山革命博物馆是地方性革命史类博物馆。位于江西省井冈山市茨坪镇红军南路5号。占地面积1.782公顷，总建筑面积20030平方米，其中展览面积10000平方米。井冈山革命博物馆馆藏文物3万余件，珍贵文献资料和历史图片2万余份，珍藏党和国家领导人、著名书画家及社会各界知名人士的墨宝珍迹千余幅。保存毛泽东、朱德等党和国家领导人重上井冈山时的影视资料数百件。其中，馆藏一级文物27件，二级文物86件，三级文物296件。同时井冈山革命博物馆还管理黄洋界保卫战遗址、毛泽东旧居等22处全国重点文物保护单位、9处省级文物保护单位和49处市级文物保护单位。近年来荣获首批全国百个爱国主义教育示范基地、首批国家一级博物馆、中国建设工程鲁班奖（国家优质工程）、新中国成立60周年百项重大经典建设工程、全国博物馆十大陈列展览精品特别奖等荣誉称号。'
        yield item
