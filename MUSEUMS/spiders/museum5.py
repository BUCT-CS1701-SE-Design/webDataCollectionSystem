# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum5'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E8%88%AA%E7%A9%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1632663?fr=aladdin']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=5
        item["museumName"]='中国航空博物馆'
        item["Location"]='北京市昌平区小汤山镇顺沙路'
        item["Link"]='https://baike.baidu.com/item/%E4%B8%AD%E5%9B%BD%E8%88%AA%E7%A9%BA%E5%8D%9A%E7%89%A9%E9%A6%86/1632663?fr=aladdin'
        item["opentime"]="8:30-17:30（周一闭馆，法定节假日除外）"
        item["telephone"]="(010)61784882"
        item["introduction"]="""中国航空博物馆是中国第一座对外开放的大型航空博物馆，该馆坐落在北京市昌平区大汤山脚下。经过多年封山育林，天然植被茂密。在72万平方米的馆区内，绿化覆盖面积达45万平方米。中国航空博物馆是首批国家一级博物馆、爱国主义教育基地、首批全国国防教育示范基地和科普教育基地、国家AAAA级旅游景区，是世界排名前五位、亚洲第一的集知识型、教育型、科技型、研究型、园林型、旅游型为一体的大型航空专业博物馆。"""
        yield item




















