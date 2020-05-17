# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume116Spider(scrapy.Spider):
    name = 'musume116'
    allowed_domains = ['yagmjng.com']
    start_urls = ['http://www.yagmjng.com/rsf/site/jinianguan/825/info/2019/81371.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=116
        item["museumName"]='延安革命纪念馆'
        item["Location"]=response.xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/p[2]/span/strong").extract_first()
        item["Link"]='http://www.yagmjng.com/'
        item["opentime"]='每日09：00至17：00（16：00停止入馆）'
        item["telephone"]=response.xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/p[4]/span/strong/text()").extract_first()
        url='http://www.yagmjng.com/rsf/site/jinianguan/zhanguanjianjie/info/2020/81013.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/p/text()").extract()
        #print(item)
        yield item 
