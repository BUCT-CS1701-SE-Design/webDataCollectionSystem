# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

class Museum60Spider(scrapy.Spider):
    name = 'museum60'
    allowed_domains = ['gthyjng.com']
    start_urls = ['http://gthyjng.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=60
        item["museumName"]='古田会议纪念馆'
        item["Location"]='福建省龙岩市上杭县古田镇古田路85号'
        item["telephone"]='0597-3641143 '
        item["Link"]='http://gthyjng.com/'
        item["opentime"]='08:00 - 17:30'
        item["introduction"]=' 古田会议纪念馆是以古田会议会址为依托建立的全面介绍古田会议历史和宣传古田会议精神，集文物收藏、资料研究和宣传教育为一体的专题类纪念馆，位于福建省龙岩市上杭县古田镇社下山西麓，处在有“北回归线荒漠带上的一颗璀璨翡翠”之称的国家4A级自然保护区——梅花山的腹地，与梅花山“华南虎园”、“红豆杉原始生态园”相距仅17公里，“红色”、“绿色”旅游资源丰富，气候宜人，环境整洁、美观、舒适，绿化率高。'
        yield item
