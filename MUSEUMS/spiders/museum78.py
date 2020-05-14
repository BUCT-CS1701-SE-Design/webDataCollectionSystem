# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem 
import re
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
class Museum78Spider(scrapy.Spider):
    name = 'museum78'
    allowed_domains = ['nyhhg.com']
    start_urls = ['http://nyhhg.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=78
        item["museumName"]='汉画馆'
        item["Link"]='http://nyhhg.com/'
        item["Location"]='南阳市卧龙区汉画街398号（卧龙区车站南路以西，卧龙路以南）'
        item["telephone"]=''
        item["opentime"]='冬季：8:30-17:00，春、夏、秋季：8:30-17:30（周一闭馆，节假日除外'
        item["introduction"]='南阳市汉画馆是目前我国建馆最早、藏品最多、规模最大的一座汉画像石刻艺术博物馆。她始创建于1935年10月。其后，三易馆舍，规模日益扩大，现收藏汉画像石总量已达两千余石。如今的南阳市汉画馆是于1999年12月建成并对外开放的新馆，2000年曾荣获“2000年度全国十大陈列精品奖”；2008年被国家文物局评定为国家一级博物馆；2009年5月18日正式对外免费开放'
        yield item