# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置


class Museum67Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

    name = 'museum67'
    allowed_domains = ['81-china.com']
    start_urls = ['http://www.81-china.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=67
        item["museumName"]='八一南昌起义纪念馆'
        item["Location"]='江西省南昌市西湖区中山路380号'
        item["telephone"]='0791 - 86613806'
        item["Link"]='http://www.81-china.com/'
        item["opentime"]='1、星期二到星期日，每天9:00 ~ 17:00;星期一闭馆，设备检修。2、参观人员凭有效身份证件排队验证、安检进馆参观（排队验证时间：上午9:00至下午16:00）'
        item["introduction"]='南昌八一起义纪念馆是为纪念南昌起义而设立的专题纪念馆。1956年成立，1959年正式对外开放，1961年被国务院公布为全国首批重点文物保护单位（所辖五处革命旧址——总指挥部旧址、贺龙指挥部旧址、叶挺指挥部旧址、朱德军官教育团旧址和朱德旧居）。作为“中国军史第一馆”自开放以来就备受瞩目，周恩来、朱德、董必武、贺龙、陈毅、彭真、江泽民、胡锦涛、习近平等老一辈无产阶级革命家以及党和国家领导人先后莅临，参观指导 '
        yield item


