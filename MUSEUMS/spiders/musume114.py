# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume114Spider(scrapy.Spider):
    name = 'musume114'
    allowed_domains = ['sxhm.com']
    start_urls = ['http://www.sxhm.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=114
        item["museumName"]='陕西历史博物馆'
        item["Location"]=response.xpath("/html/body/div[3]/div/div[2]/p[3]/text()").extract_first()
        item["Link"]='http://www.sxhm.com/'
        item["opentime"]='周二至周日 09:00-17:30；遇法定节假日周一除外'
        item["telephone"]=response.xpath("/html/body/div[3]/div/div[2]/p[1]/text()").extract_first()
        url='http://www.sxhm.com/index.php?ac=article&at=list&tid=230'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("/html/body/div[3]/div[2]/div[2]/p/span/text()").extract()
        #print(item)
        yield item 
