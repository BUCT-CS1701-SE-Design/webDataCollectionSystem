# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume130Spider(scrapy.Spider):
    name = 'musume130'
    allowed_domains = ['xabwy.com']
    start_urls = ['http://www.xabwy.com/index.aspx']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=130
        item["museumName"] ='吐鲁番博物馆'
        item["Location"] ='吐鲁番市高昌区木纳尔路1268号'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]=''
        item["opentime"] = '周二至周日10:00-18:00'
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]='0995-7619644;0995-7619645;0995-7619650'
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
        item["introduction"] = '吐鲁番博物馆位于新疆维吾尔自治区吐鲁番市高昌区木纳尔路1268号。是新疆第二大博物馆，国家一级博物馆，国家4A级旅游景区，全国社会科学普及基地，自治区级爱国主义教育基地，是集文物收藏展陈、文化遗产保护与研究、社会科学宣传教育等职能于一体的国有综合类博物馆。'
        #item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        #item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
