# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum20'
    allowed_domains = ['www.hdmuseum.org']
    start_urls = ['http://www.hdmuseum.org/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=20
        item["museumName"]='邯郸市博物馆'
        item["Location"]='河北省邯郸市中华北大街45号'
        item["Link"]='http://www.hdmuseum.org/'
        item["opentime"]="夏季：9:00-11:30，14:45-17:30 冬季：9:00-11:30，14:00-17:00 周一全天闭馆"
        item["telephone"]="电话：0310-3012739"
        item["introduction"]="""邯郸市博物馆成立于1984年，是国家二级博物馆和河北省爱国主义教育基地。主体建筑的前身是1968年建成的"毛泽东思想胜利万岁邯郸展览馆"，现为河北省文物保护单位。2009年实行免费开放。"""
        yield item
