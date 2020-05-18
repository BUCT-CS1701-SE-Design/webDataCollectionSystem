# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline

class Collection75Spider(scrapy.Spider):
    name = 'collection13'
    allowed_domains = ['www.bjp.org.cn']
    start_urls = ['http://www.bjp.org.cn/art/2014/1/10/art_27_1678.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1677.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1676.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1675.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1674.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1673.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1672.html','http://www.bjp.org.cn/art/2014/1/10/art_27_1671.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    def parse(self, response):
        item=collection75Item()
        item["museumID"]=13
        item['collectionName']=response.xpath("//meta[@name='title']/@content").extract_first()
        item['collectionImage']='www.bjp.org.cn'+response.xpath("//p[@style='text-align:center;']/img/@src").extract_first()
        list=response.xpath("//p[@style='text-indent:2em;']/text()").extract()
        content=''
        for i in list:
            content+=i
        item['collectionIntroduction']=content
        if item['collectionIntroduction']!='':
         yield item


        








