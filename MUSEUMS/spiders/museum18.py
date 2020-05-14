# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum18'
    allowed_domains = ['www.hebeimuseum.org.cn']
    start_urls = ['http://www.hebeimuseum.org.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=18
        item["museumName"]='河北博物院'
        item["Location"]='河北省石家庄市东大街4号'
        item["Link"]='http://www.hebeimuseum.org.cn/'
        item["opentime"]="开放时间：周二至周日9：00-17：00"
        item["telephone"]="开放咨询86062086;团体预约:85286681  86049534"
        item["introduction"]="""河北博物院的前身是河北省博物馆。2014年6月9日，河北博物院揭牌成立，总建筑面积53128平方米，展览面积22000余平方米， 文物藏品15万件，其中一级品334件（套），二级品1910件（套），三级品16313件（套），以满城汉墓出土文物、河北古代四大名窑瓷器、元青花、石刻佛教造像、明清地方名人字画以及抗日战争时期文物最具特色。另外，院内藏书5万余册，不少是明清善本图书，为河北省地方志主要收藏单位之一（截至2014年末）。"""
        yield item