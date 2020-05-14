# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum19'
    allowed_domains = ['www.xbpjng.cn']
    start_urls = ['http://www.xbpjng.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=19
        item["museumName"]='西柏坡纪念馆'
        item["Location"]='河北省平山县西柏坡村'
        item["Link"]='http://www.xbpjng.cn/'
        item["opentime"]="淡季：上午9：00-下午4：30；旺季：上午9：00-下午5：00"
        item["telephone"]="电话：0311-82851355"
        item["introduction"]="""西柏坡位于河北省平山县中部，是解放战争时期中央工委、中共中央和解放军总部的所在地。1947年5月，刘少奇、朱德率中央工委进驻西柏坡。1948年5月，毛泽东、周恩来、任弼时率中央前委和解放军总部到西柏坡与中央工委汇合。在这里，毛泽东和他的战友们召开了中国共产党全国土地会议，通过了《中国土地法大纲》，实现了“耕者有其田”；指挥了辽沈、淮海、平津三大战役，决定了中国的命运；召开了中国共产党七届二中全会，描绘了新中国宏伟的蓝图。1949年3月23日，中共中央和解放军总部离开西柏坡，赴京建国。新中国从这里走来。"""
        yield item

