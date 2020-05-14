# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum13'
    allowed_domains = ['www.bjp.org.cn']
    start_urls = ['http://www.bjp.org.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=13
        item["museumName"]='北京天文馆'
        item["Location"]='北京西直门外大街138号'
        item["Link"]='http://www.bjp.org.cn/'
        item["opentime"]="开放时间：周三至周日 9:00-16:30（16:00停止入馆）"
        item["telephone"]="电话：010-68312517"
        item["introduction"]="""北京天文馆坐落于北京市西城区西直门外大街138号，占地面积20,000平方米，建筑面积26,000平方米，于1957年正式对外开放，是我国第一座大型天文馆，也是当时亚洲大陆第一座大型天文馆。五十多年来，北京天文馆以其独特的演示手段，吸引了一代又一代的观众。现为国家AAAA级旅游景区。北京天文馆包含A、B两馆，共4个科普剧场。A馆天象厅是我国大陆地区最大的地平式天象厅，内部设备处于世界领先水平。其中，蔡司九型光学天象仪和世界上分辨率最高的全天域数字投影系统，不仅能为场内400名观众逼真还原地球上肉眼可见的9,000余颗恒星，高达8K分辨率的球幕影像，还能实现虚拟天象演示、三维宇宙空间模拟、数字节目播放等多项功能。"""
        yield item








