# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }


class Museum66Spider(scrapy.Spider):
    name = 'museum66'
    allowed_domains = ['rjjng.com.cn']
    start_urls = ['http://www.rjjng.com.cn/new_index.html']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=66
        item["museumName"]='中央革命根据地纪念馆'
        item["Location"]='江西省瑞金市城西龙珠路1号'
        item["telephone"]='0797-2522063'
        item["Link"]='http://www.rjjng.com.cn/new_index.html'
        item["opentime"]='8:30 ----- 17:30（夏季）8:30 ----- 17:00（冬季）（旧址景区全年开放，博物馆星期一闭馆检修，法定节假日除外）'
        item["introduction"]='瑞金中央革命根据地历史博物馆是为纪念土地革命战争时期中国共产党及其领袖毛泽东、朱德、周恩来等老一辈无产阶级革命家直接领导创建中央革命根据地和红一方面军，缔造中华苏维埃共和国的历史而建立的专业性纪念馆。1953年筹建瑞金革命纪念馆，1958年正式开馆，1994年更名为“瑞金中央革命根据地纪念馆”。2007年10月，江泽民同志题写了“中央革命根据地历史博物馆”馆名。是首批全国百个爱国主义教育示范基地之一、全国青少年教育基地、全国中小学爱国主义教育基地等，2008年评为首批国家一级博物馆。 '
        yield item

