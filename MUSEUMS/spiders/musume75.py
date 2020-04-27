# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume75Spider(scrapy.Spider):
    name = 'musume75'
    allowed_domains = ['chnmus.net']
    start_urls = ['http://www.chnmus.net']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=75
        item["museumName"]='河南博物院'
        item["Location"]='河南省郑州市金水区农业路8号'
        item["Link"]='http://www.chnmus.net'
        item["opentime"]=response.xpath("//div[@class='view2']/div[@class='serve']/p[@class='serve_time']/text()").extract_first()
        item["telephone"]=response.xpath("//div[@class='view2']/div[@class='serve']/p[@class='serve_tel']/text()").extract_first()
        url='http://www.chnmus.net'+response.xpath("//div[@class='gailan_con']/a/@href").extract_first()
        # 处理详情页
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("//div[@class='tab-bd']/div[1]/div[@class='view2']/p/text()").extract()
        #print(item)
        yield item 
