# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置


class Museum59Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
    name = 'museum59'
    allowed_domains = ['museum.fjsen.com']
    start_urls = ['http://museum.fjsen.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=59
        item["museumName"]='福建博物院'
        item["Location"]='福建省福州市鼓楼区湖头街96号 '
        item["telephone"]=''
        item["Link"]='http://museum.fjsen.com/'
        item["opentime"]='展厅开放时间调整为每周五至周日9：00－16：30（五一期间正常开放），院区开放时间为每日6：00－22：30'
        item["introduction"]='福建博物院坐落于福州市西湖公园，始建于1933年，原名福建省立科学馆。1953年成立福建省博物馆，2002年10月新馆建成，同时更名为福建博物院。博物院占地面积6公顷，建筑面积3.6万平方米。整个建筑共投资2.7亿元，包括地下一层、地上三层。新馆展览面积1.5万平方米，共有15个展厅，包括7个基本陈列展厅和6个临时展厅。此外新馆还设有贵宾厅、会议室、具备六声道同声传译且可放映投射电视可容纳345人的多功能学术报告厅和影象厅'
        yield item
