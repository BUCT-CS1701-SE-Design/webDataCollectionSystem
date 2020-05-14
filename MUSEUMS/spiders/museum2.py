# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum2'
    allowed_domains = ['cstm.cdstm.cn']
    start_urls = ['http://cstm.cdstm.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=2
        item["museumName"]='中国科学技术馆'
        item["Location"]='北京市朝阳区北辰东路5号'
        item["Link"]='http://cstm.cdstm.cn/'
        item["opentime"]=response.xpath("//p[@class='index-time-info-cont']/span[@class='index-time-info-text']/em[@class='cont-text color666 float-l text12']/text()").extract_first()
        item["telephone"]='59041000'
        url='http://cstm.cdstm.cn/e/action/ListInfo/?classid=87'
        yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list = response.xpath("//div[@class='fen-info-cont']/p")
        content= ''
        for p in p_list:
            x= p.xpath("./text()").extract_first()
            if x!=None:
                content+=x
        item["introduction"]=content
        yield item

