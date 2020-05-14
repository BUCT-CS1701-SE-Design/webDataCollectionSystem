# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum22'
    allowed_domains = ['www.coalmus.org.cn']
    start_urls = ['http://www.coalmus.org.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=22
        item["museumName"]='中国煤炭博物馆'
        item["Location"]='山西省太原市迎泽西大街2号'
        item["Link"]='http://www.coalmus.org.cn/'
        item["opentime"]="8:00-18:00（17:00停止售票，全年开放）"
        item["telephone"]="电话：0351-6180108"
        item["introduction"]="""中国煤炭博物馆（以下简称中煤博）是根据1982年11月10日全国人大五届五次会议提案，国务院批准建设唯一的国家级煤炭行业博物馆，是原煤炭部创建的山西省境内唯一中字头国字号行业博物馆，为副厅级建制公共文化公益事业单位。在选址过程中，山西省委省政府积极争取并提供位置优越的建馆用地，中煤博最终落户山西。1983年4月12日原煤炭部立项建设，1984年原煤炭部决定中煤博委托山西矿业学院建设，1988年原煤炭部变更隶属关系，由山西矿业学院改变为山西煤炭工业管理局管理。1989年9月30日开馆。1990年3月原山西煤管局为落实原煤炭部关于中煤博“以馆养馆”的指示精神，在中煤博设立“山西统配煤矿综合经营总公司”（以下简称总公司）牌子，行使原山西煤管局综合经营处对六局和直属单位多种经营和集体企业的管理职能，与中煤博实行“两块牌子，一套人马”的管理体制，以多种经营支撑文博事业的正常运营。1990年11月原山西煤管局将山西煤矿安全培训中心（全额事业单位）65人及部分资产划转中煤博。1998年9月30日中煤博由原煤炭部下放山西省。"""
        yield item



