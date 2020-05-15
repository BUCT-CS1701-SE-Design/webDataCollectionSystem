# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置


class Museum68Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
    name = 'museum68'
    allowed_domains = ['aymuseum.com']
    start_urls = ['http://www.aymuseum.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=68
        item["museumName"]='安源路矿工人运动纪念馆'
        item["Location"]='江西省萍乡市安源区正街路'
        item["telephone"]='(0799)7101123'
        item["Link"]='http://www.aymuseum.com/'
        item["opentime"]='星期二至星期日开放   星期一闭馆检修；夏季9:00——17:30（17:00停止入内） 冬季9:00——17:00（16:30停止入内）'
        item["introduction"]='安源是中国工人运动的摇篮，是中国近代工业发祥地，是湘赣边界秋收起义策源地和主要爆发地。安源路矿工人运动纪念馆是为征集和保护安源工人运动的文物，研究和宣传安源革命斗争历史而于1956年创建的专题类博物馆，1968年兴建了陈列大楼，1984年邓小平同志为纪念馆题写馆名。馆区面积10万平方米，建筑面积21341平方米，展厅面积3567平方米（其中陈列馆面积3245平方米，安源工运时期廉政建设陈列馆面积322平方米）。我馆现有馆藏文物与资料5000余件，其中一级文物61件/套，二级文物67件/套，三级文物2050件/套；负责保护和宣传的文物保护单位共14处，其中全国重点文物保护单位4处，省级文物保护单位8处，市级文物保护单位1处,区级文物保护单位1处。下设有安源工运时期廉政建设陈列馆和中共湖南省委在安源革命活动展览馆两个展览馆。'
        yield item



