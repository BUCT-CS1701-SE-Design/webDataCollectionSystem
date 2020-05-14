# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection11'
    allowed_domains = ['www.chnmuseum.cn']
    start_urls = ['http://www.chnmuseum.cn/zp/zpml/201812/t20181218_23312.shtml','http://www.chnmuseum.cn/zp/zpml/201812/t20181218_23313.shtml','http://www.chnmuseum.cn/zp/zpml/201812/t20181218_23372.shtml','http://www.chnmuseum.cn/zp/zpml/201812/t20181218_23723.shtml','http://www.chnmuseum.cn/zp/zpml/201812/t20181218_25359.shtml']
    
    def parse(self, response):
        item=collection75Item()
        item["museumID"]=11
        item['collectionName']=response.xpath("//div[@class='cj_ercom_wai cj_huawenbg1']/div[@class='cj_baici_ma']/div[@class='cj_dycp_lef']/a/img/@alt").extract_first()
        item['collectionImage']='http://www.chnmuseum.cn/zp/zpml/201812'+response.xpath("//div[@class='cj_ercom_wai cj_huawenbg1']/div[@class='cj_baici_ma']/div[@class='cj_dycp_lef']/a/img/@src").extract_first()[1:]
        content=""
        p_list=response.xpath("//div[@class='wwms']/p/text()").extract()
        for p in p_list:
            content+=p
        item['collectionIntroduction']=content
        yield item


        







