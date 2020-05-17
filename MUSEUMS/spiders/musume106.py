# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume106Spider(scrapy.Spider):
    name = 'musume106'
    allowed_domains = ['www.zgshm.cn']
    start_urls = ['http://www.zgshm.cn/index.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=106
        item["museumName"]='自贡市盐业历史博物馆'
        item["Location"]=response.xpath("normalize-space(/html/body/div[6]/div/div[2]/p[1])").extract_first()
        item["Location"] = str(item["Location"]).replace(u'\u3000', u'')

        item["Link"]='http://www.zgshm.cn/index.html'
        item["opentime"]='1月1日-12月31日 08:30-16:30'
        item["telephone"]=response.xpath("normalize-space(/html/body/div[6]/div/div[2]/p[2]/text())").extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\u3000', u'  ')

        url='http://www.zgshm.cn/content.jsp?id=297e0fc26362ffbb016380a82d360199'#  +response.xpath("/html/body/div[1]/ul//a/@href").extract_first()
        # 处理详情页r
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("normalize-space(/html/body/div[3]/div/div[4]/p/span)").extract()
        item["telephone"] = str(item["telephone"]).replace(u'\u3000', u' ')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
