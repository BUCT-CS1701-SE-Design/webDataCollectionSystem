# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum24'
    allowed_domains = ['www.nmgbwy.com']
    start_urls = ['http://www.nmgbwy.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=24
        item["museumName"]='内蒙古博物院'
        item["Location"]='内蒙古呼和浩特市新城区新华东街27号'
        item["Link"]='http://www.nmgbwy.com/'
        item["opentime"]="夏季：9:00-17:30，冬季：9:30-17:00；周一全天闭馆"
        item["telephone"]="预约电话：0471-4614333  咨询电话：0471-4614000"
        item["introduction"]="""内蒙古博物院的前身是内蒙古博物馆，始建于1957年，2008年改称内蒙古博物院，现在是国家一级博物馆，是内蒙古自治区最大的集文物收藏、研究、展示于一体的综合性博物馆，也是全国爱国主义教育基地，全国民族团结进步先进单位。内蒙古博物院主体建筑面积64000平方米，展厅面积15000平方米。内蒙古博物院设有展览陈列部、文物保管研究部、文物保护中心、社会教育部、安全保卫部、人事部、办公室、财务部、文化产业部、文物保护研究信息中心等十个部室，下辖国家文物出入境审核内蒙古管理处、大窑旧石器时代文物保护管理所等机构。"""
        yield item
