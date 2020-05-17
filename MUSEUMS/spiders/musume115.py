# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume115Spider(scrapy.Spider):
    name = 'musume115'
    allowed_domains = ['bmy.com.cn']
    start_urls = ['http://www.bmy.com.cn/html/public/dl/0f082ba612ca4ebc8ffe58958470c487.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=115
        item["museumName"]='秦始皇帝陵兵马俑博物馆'
        item["Location"]='河南省郑州市金水区农业路8号'
        item["Link"]='http://bmy.com.cn/'
        item["opentime"]=response.xpath("/html/body/div[4]/div[1]/div[3]/div/div[2]/div[2]/text()").extract_first()
        item["telephone"]=response.xpath("/html/body/div[3]/div/div/div[2]/p/span/text()").extract_first()
        url='http://www.bmy.com.cn/html/gov/jggk/8eaf8a3015b643b7adcb9d6815e0f845.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]='秦始皇兵马俑博物馆位于陕西省西安市临潼区秦陵镇，成立于1975年11月，原为秦始皇兵马俑筹建处，于1979年10月1日正式开馆，建于临潼县东7.5公里的骊山北麓的秦始皇帝陵兵马俑坑遗址上，西距西安37.5公里；和丽山园合称秦始皇帝陵博物院。'
        #print(item)
        yield item 
