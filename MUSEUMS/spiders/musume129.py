# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume129Spider(scrapy.Spider):
    name = 'musume129'
    allowed_domains = ['xabwy.com']
    start_urls = ['http://www.xabwy.com/index.aspx']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=129
        item["museumName"] ='新疆维吾尔自治区博物馆'
        item["Location"] ='乌鲁木齐市沙依巴克区西北路581号'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]=''
        #item["opentime"] = response.xpath('normalize-space(/html/body/div[4]/div[2]/div[2]/text()[1])').extract_first()
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        item["opentime"] = '每周二至周日的10：30—18：00'
        item["telephone"]='0991-4536436'
        #item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        #item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='http://www.xabwy.com/Statics/2020.01/66.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = '新疆维吾尔自治区博物馆位于乌鲁木齐市西北路132号，是省级综合性地志博物馆，是新疆维吾尔自治区的文物和标本收藏保护、科学研究和宣传教育机构。新疆维吾尔自治区博物馆于1959年正式成立，原馆初步设计是农业展览馆，为山字形平房建筑，1962年迁至现址改为博物馆并对外开放。“新疆维吾尔自治区博物馆”馆名是老一代革命家朱德委员长1959年来新疆视察工作时为题写的。2005年新馆建成，建筑面积17288平方米，地下一层、地上二层，主体高18.5米，该馆科研工作以馆藏文物为重点。第一批全国中小学生研学实践教育基地。'
        #item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        #item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
