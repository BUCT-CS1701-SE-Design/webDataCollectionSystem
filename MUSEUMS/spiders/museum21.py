# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum21'
    allowed_domains = ['www.shanximuseum.com']
    start_urls = ['http://www.shanximuseum.com/index.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=21
        item["museumName"]='山西博物院'
        item["Location"]='山西省太原市汾河西畔滨河西路北段13号'
        item["Link"]='http://www.shanximuseum.com/index.html'
        item["opentime"]="开馆时间9:00  停止入馆16:00  闭馆时间17:00"
        item["telephone"]="联系电话：4006446365"
        item["introduction"]="""山西博物院位于太原市秀美的汾河西畔，占地168亩，建筑面积5.1万平方米，总投资近4亿元人民币，是目前国内屈指可数的大型现代化、综合性博物馆之一，为国家“九五”重点建设工程，也是山西省建国以来投资规模最大的文化基础设施。"""
        yield item


