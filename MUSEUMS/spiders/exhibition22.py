# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition22'
    allowed_domains = ['www.coalmus.org.cn']
    start_urls = ['http://www.coalmus.org.cn/html/list_1612.html']
    def parse(self, response):
        names=['洗煤厂设备流程模拟',
               '煤炭发电原理',
               '煤炭与蒸气机的发明',
               '矿井的大脑·调度中心',
               '5米长的硅化木',
               '砌起的模拟矿井·运输大巷',
               '为开采光明的人提供光明·矿灯充电处']
        imgs=['http://www.coalmus.org.cn/UploadFiles/2016-01/20074222312325613.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742222313582736.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742222325298119.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/20074231334890322.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742022233428746.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/2007423126897976.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/20074231322143122.jpg',
               ]
        intros=['洗煤厂设备流程模拟',
                '煤炭发电原理',
                '煤炭与蒸气机的发明',
                '矿井的大脑·调度中心',
                '5米长的硅化木',
                '砌起的模拟矿井·运输大巷',
                '为开采光明的人提供光明·矿灯充电处']
        for i in range(7):  
            item=exhibition75Item()
            item["museumID"]=22
            item["exhibitionTheme"]=names[i]
            item["exhibition_picture"]=imgs[i]
            item["exhibitionIntroduction"]=intros[i]
            yield item  





