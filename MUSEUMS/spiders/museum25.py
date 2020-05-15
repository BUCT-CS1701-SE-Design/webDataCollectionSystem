# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum25'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%84%82%E5%B0%94%E5%A4%9A%E6%96%AF%E5%8D%9A%E7%89%A9%E9%A6%86/4468890?fr=aladdin']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=25
        item["museumName"]='鄂尔多斯博物馆'
        item["Location"]='内蒙古鄂尔多斯市康巴什区文化西路南5号'
        item["Link"]='https://baike.baidu.com/item/%E9%84%82%E5%B0%94%E5%A4%9A%E6%96%AF%E5%8D%9A%E7%89%A9%E9%A6%86/4468890?fr=aladdin'
        item["opentime"]="每周二至周日9：00-17：00 周一闭馆"
        item["telephone"]="(0477)8390997"
        item["introduction"]="""鄂尔多斯博物馆是一所综合性博物馆，位于鄂尔多斯市康巴什新区，于2006年开工建设，占地面积27760平方米，建筑面积41227平方米，为地下一层，地上四层，局部八层。"""
        yield item




















