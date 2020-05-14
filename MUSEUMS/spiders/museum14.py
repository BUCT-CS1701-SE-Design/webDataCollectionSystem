# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum14'
    allowed_domains = ['www.pgm.org.cn']
    start_urls = ['http://www.pgm.org.cn/pgm/index.shtml']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=14
        item["museumName"]='恭王府'
        item["Location"]='北京市西城区柳荫街甲14号'
        item["Link"]='http://www.pgm.org.cn/pgm/index.shtml'
        item["opentime"]="开馆时间8:30  停止检票时间16:10  闭馆时间17:00 （除法定节假日外，周一全天闭馆）"
        item["telephone"]="联系电话：010-83288149"
        item["introduction"]="""恭王府博物馆隶属于中华人民共和国文化和旅游部，是集文物保护、博物馆建设、旅游开放、文化空间营造、文化产业开发等职能为一体的综合性公共文化机构。1982年列入全国重点文物保护单位，2012年晋级国家5A级旅游景区，2017年被评为国家一级博物馆。作为现今北京保存最为完整且唯一对社会开放的清代王府，恭王府已经历了240余年的风雨沧桑。自1978年启动搬迁腾退到2008年迎来全面开放，恭王府人用30年的努力实现了周恩来总理的遗愿。恭王府博物馆作为建立在恭王府遗址基础上，以王府文化为研究展示传播核心的社区博物馆，着力建设“平安王府、学术王府、数字王府、公众王府”。"""
        yield item

















