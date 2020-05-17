# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置



class Museum73Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
    name = 'museum73'
    allowed_domains = ['ytmuseum.com']
    start_urls = ['http://www.ytmuseum.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=73
        item["museumName"]='烟台市博物馆'
        item["Location"]='山东省烟台市南大街61号'
        item["telephone"]='0535-6232976'
        item["Link"]='http://www.ytmuseum.com/'
        item["opentime"]='5月—10月 9：00-17：00（16:30停止入场）    11月—4月 9：00-16：30（16:00停止入场）    每周一闭馆（法定节假日除外） '
        item["introduction"]=' 烟台民俗博物馆成立于2010年，馆址设在烟台福建会馆，隶属于烟台市博物馆。福建会馆始建于清光绪年间（1884年），竣工于1906年，时有“鲁东第一工程”之称，是具有闽南风格的古建筑群。馆内有妈祖文化陈列以及烟台近代家居陈列等多个展厅，其展览内容丰富多彩，形式新颖独特，是集中展示烟台地方民俗风情和弘扬妈祖文化的专题博物馆。'
        yield item

