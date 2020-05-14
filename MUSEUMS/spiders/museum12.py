# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum12'
    allowed_domains = ['www.ciae.com.cn/index.html']
    start_urls = ['http://www.ciae.com.cn/index.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=12
        item["museumName"]='中国农业博物馆'
        item["Location"]='北京市朝阳区东三环北路16号'
        item["Link"]='http://www.ciae.com.cn/index.html'
        item["opentime"]="博物馆开放时间：9：00—16：00"
        item["telephone"]="展览咨询电话:010-65096688"
        item["introduction"]="""全国农业展览馆和中国农业博物馆是两块牌子、一个机构，为中华人民共和国农业农村部直属事业单位。全国农业展览馆是1958年经国务院批准兴建的首都十大建筑之一，其地理位置、规模、布局和风格均由周恩来总理亲自审定，1959年9月正式落成并对外开放。中国农业博物馆是1983年7月经国务院批准，在全国农业展览馆基础上筹建的国家级专业博物馆，1986年9月正式对外开放，2012年被评为国家一级博物馆。"""
        yield item







