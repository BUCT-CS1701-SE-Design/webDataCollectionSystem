# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

class Museum55Spider(scrapy.Spider):
    name = 'museum55'
    allowed_domains = ['nbmuseum.cn']
    start_urls = ['http://nbmuseum.cn/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=55
        item["museumName"]='宁波博物馆'
        item["Location"]='浙江省宁波市鄞州区首南中路1000号'
        item["telephone"]='0574-82815588'
        item["Link"]='http://nbmuseum.cn/'
        item["opentime"]='宁波博物馆将于2020年5月1日起，实行临时闭馆，恢复开放时间另行通知。'
        item["introduction"]='宁波博物馆是国家一级博物馆、全国最具创新力博物馆，是以展示宁波人文、历史和艺术为主，具有地域特色的综合性博物馆，位于鄞州区首南中路1000号，2008年12月5日免费对外开放。宁波博物馆建筑为首位中国籍“普利兹克建筑奖”得主王澍“新乡土主义”风格的代表作，总建筑面积3万平方米，主体建筑长144米，宽65米，高24米，外立面采用浙东地区瓦；1墙和竹纹理混凝土，主体三层、局部五   层，主体二层以下集中布局，两层以上建筑开裂、微微倾斜，演变成抽 象的山体，将宁波地域文化特征、传统建筑元素与现代建筑形式和工艺融为一体，造型简约而富有灵动，外观严谨而颇具创意，充分体现了博物馆本身也是一件“展品”的理念'
        yield item

