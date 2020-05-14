# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

class Museum69Spider(scrapy.Spider):
    name = 'museum69'
    allowed_domains = ['qingdaomuseum.com']
    start_urls = ['http://www.qingdaomuseum.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=69
        item["museumName"]='青岛市博物馆'
        item["Location"]='山东省青岛市崂山区梅岭东路51号'
        item["telephone"]='(0532)88896286'
        item["Link"]='http://www.qingdaomuseum.com/'
        item["opentime"]='上午9:00~下午17:00 ，16:30停止入馆，周一闭馆（法定节假日除外）'
        item["introduction"]='青岛市博物馆是中国文化瑰宝和城市记忆的一个重要载体，是青岛唯一的国家一级博物馆和地方综合地志类博物馆。根据习近平总书记“让收藏在博物馆里的文物活起来”的要求，青博以“开放办馆”为宗旨，以“服务社会”为己任，一系列重磅举措让近60年历史的博物馆焕发出前所未有的生命力。耗时四年的文物普查，将24万余件馆藏的家底摸清摸透，无数由于历史原因蒙尘的珍贵文物得以再度显耀于世。日趋成熟的策展人制度不仅深层挖掘馆藏，更整合国内外优秀资源，让观众在感官的纵情饕餮下更能深刻体会历史与美带来的满足。自成品牌的社教活动不断推陈出新，吸引着越来越多的市民走进博物馆的同时更注重如何让博物馆走出去，使青博真正的成为城市的博物馆，社区的博物馆，人民的博物馆！'
        yield item
