# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume125Spider(scrapy.Spider):
    name = 'musume125'
    allowed_domains = ['dha.ac.cn']
    start_urls = ['https://www.dha.ac.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=125
        item["museumName"] ='敦煌研究院'
        item["Location"] ='甘肃省酒泉市敦煌市'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='https://www.dha.ac.cn/'
        item["opentime"] =''
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]='敦煌研究院网络中心 : 0937-8869123'
        #item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        #item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='https://www.dha.ac.cn/'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = '敦煌研究院的前身是1944年成立的国立敦煌艺术研究所，1950年改组为敦煌文物研究所，1984年扩建为敦煌研究院。敦煌研究院是敦煌学研究的科研单位。也是保护敦煌石窟（莫高窟、榆林窟、西千佛洞）和麦积山石窟、炳灵寺石窟、北石窟寺等其它文物机构的文博单位；是爱国主义教育基地，也是旅游接待单位。常书鸿促成了国立敦煌艺术研究所的成立，他视莫高窟为“家”，被誉为“敦煌守护神”，这5个字就镌刻在常书鸿先生的墓碑上。2017年5月，在庆祝“国际博物馆日”之际，国家一级博物馆授牌仪式近日在北京举行，敦煌研究院成功晋级，成为国家文物局第三批新增的34家国家一级博物馆的其中之一。2019年8月31日，由敦煌研究院等单位联合摄制，赵声良担任学术主持的大型纪录片《莫高窟与吴哥窟的对话》在敦煌国际会展中心首映。该纪录片的首映是第四届丝绸之路(敦煌)国际文化博览会与第九届敦煌行·丝绸之路国际旅行节闭幕式的重要活动之一。'
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
