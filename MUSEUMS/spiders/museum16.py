# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum16'
    allowed_domains = ['www.tjnhm.com']
    start_urls = ['https://www.tjnhm.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=16
        item["museumName"]='天津自然博物馆'
        item["Location"]='友谊路31号，银河广场(近平江道)'
        item["Link"]='https://www.tjnhm.com/'
        item["opentime"]="开放时间:9点-16点"
        item["telephone"]="电话：022-23347988  022-23359807"
        item["introduction"]="""天津自然博物馆新馆位于天津文化中心、原天津博物馆内，占地面积为5万平方米，总建筑面积为3.5万平方米，展示面积1.4万平方米，包括常设陈列区、临展区、体验娱乐区、科普教育区四部分。馆藏生物标本40万件，其中一、二级珍品1282件，模式标本1452件。新馆陈列以“家园”为主题，是全国第一个主题单元化、全景式展示的自然探索、科学体验、科学教育的自然史博物馆。"""
        yield item



















