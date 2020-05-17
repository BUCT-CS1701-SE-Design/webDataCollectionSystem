# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume113Spider(scrapy.Spider):
    name = 'musume113'
    allowed_domains = ['tibetmuseum.com.cn']
    start_urls = ['http://www.tibetmuseum.com.cn/zh-CN/index?navIndex=0']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=113
        item["museumName"]='西藏博物馆'
        item["Location"]='西藏自治区拉萨市城关区民族南路2号'
        item["Link"]='http://www.tibetmuseum.com.cn'
        item["opentime"]='夏秋季(5月1日至10月31日):09:30-17:30 (17:00游客停止入场)冬春季(11月1日至次年4月30日):10:30-17:00(16:30游客停止入场)'
        item["telephone"]='0891-6835244 0891-6812210'
        url='http://www.tibetmuseum.com.cn/zh-CN/brief/historyRecord?isNav=yes&navIndex=1'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]='西藏博物馆是由国家直接投资兴建的西藏自治区唯一一座国家一级博物馆。 1999年10月，中华人民共和国成立50周年和西藏民主改革40周年之际落成开馆。 博物馆占地面积5万余平方米，展厅面积1万平方米，整体建筑具有鲜明的藏族传统建筑艺术特色， 同时兼具现代建筑的实用特点与功能，是传统与现代建筑风格有机结合的典范。 '
        #print(item)
        yield item 
