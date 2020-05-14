# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum10'
    allowed_domains = ['www.zkd.cn']
    start_urls = ['http://www.zkd.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=10
        item["museumName"]='周口店遗址博物馆'
        item["Location"]='北京城西南房山区周口店龙骨山脚下'
        item["Link"]='http://www.zkd.cn/'
        item["opentime"]="09:00至16:30（16:00停止入园）"
        item["telephone"]="咨询电话：010-69301090"
        item["introduction"]="""周口店遗址博物馆新馆位于周口店遗址南侧约500米，是展示遗址深厚文化的重要组成部分，面积8000余平方米，粗粝、刚毅的建筑外观源于“北京人”最早制造和使用的工具——石器。馆藏文物7000多件，展出文物1000多件。博物馆设有临时展览、基本陈列和4D影院，涵盖了科普互动展项、模拟场景、纪念品销售、公共服务等内容。 周口店遗址1961年被国务院公布为全国重点保护单位；1987年被联合国教科文组织列入世界文化遗产名录；1992年被北京市政府授予青少年科普教育基地称号；1997年被中宣部评为全国百家爱国主义教育示范基地之一；2008年、2010年先后被国家文物局评为国家一级博物馆、国家考古遗址公园；2011年被联合国教科文组织亚太地区世界遗产培训与研究中心授予“世界遗产青少年教育基地”称号；2012年被中国科学技术协会授予“全国科普教育基地”称号。"""
        yield item





