# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum23'
    allowed_domains = ['www.balujun.cn']
    start_urls = ['http://www.balujun.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=23
        item["museumName"]='八路军太行纪念馆'
        item["Location"]='山西省长治市武乡县城太行街363号'
        item["Link"]='http://www.balujun.cn/'
        item["opentime"]="冬季：8:30—18:00  夏季：8:30—18:30"
        item["telephone"]="电话：0355-6437583"
        item["introduction"]="""八路军太行纪念馆（Taihang Memorial Museum of the Eighth Route Army）,是中国唯一全面反映八路军抗战历史的大型革命纪念馆，同时也是国家级抗战纪念设施、国家一级博物馆，集收藏、展览、研究、宣传于一体的综合性红色旅游经典景区。"""
        yield item









