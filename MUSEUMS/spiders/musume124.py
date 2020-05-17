# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume124Spider(scrapy.Spider):
    name = 'musume124'
    allowed_domains = ['tssbwg.com.cn']
    start_urls = ['http://www.tssbwg.com.cn/index.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=124
        item["museumName"] ='天水市博物馆'
        item["Location"] ='甘肃省天水市秦州区伏羲路110号'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='http://www.tssbwg.com.cn/'
        item["opentime"] = '每天上午8:00 - 12:00；下午 14:00 - 18:00 开放'
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]='0938-8291377'
        #item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        #item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='http://www.tssbwg.com.cn/html/2013/zzjg_1127/218.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] ='天水市博物馆是国家一级博物馆，担负着天水地域内历史文物、民俗文物的征集、保管修复、陈列展览、科学研究和全国重点文物保护单位天水伏羲庙、天水民俗博物馆的保护维修与旅游资源开发利用以及国家级非物质文化遗产——“太昊伏羲祭典”礼仪的保护与传承等多项工作任务。我馆成立于1979年，正县级建制，隶属于天水市文化和旅游局，1986年由天水城隍庙搬迁至天水伏羲庙，形成馆庙合一体制。现占地面积35000平方米，建筑面积8361平方米。现有职工260人，其中正式职工99人。内设办公室、文物保管部、陈展宣传部、接待服务部、天水民俗博物馆、保卫科、文物保护修复中心、历史文化研究部、古建筑保护与园林部、太昊伏羲祭典保护传承中心、美术研究部、文化旅游部、文物考古研究所等13个业务部室。有馆长、书记1人，副馆长4人，部室主任（科级干部）19人。历史文化陈列馆有九个陈列展厅，两个临时展厅，一座高清数字影院，2009年10月、2011年12月天水市博物馆、天水民俗博物馆通过升级改造，分别实现了免费对外开放。'
        #item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        #item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
