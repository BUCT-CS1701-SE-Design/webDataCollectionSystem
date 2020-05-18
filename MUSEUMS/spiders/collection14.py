# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline

class Collection75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection14'
    allowed_domains = ['www.pgm.org.cn']
    start_urls = ['http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16657&decade.id=',
                  'http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16659&decade.id=',
                  'http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16660&decade.id=',
                  'http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16664&decade.id=',
                  'http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16665&decade.id=',
                  'http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16687&decade.id=',
                  'http://www.pgm.org.cn/newPgm_Collection/findCollectById?&collect.id=16756&decade.id=']
    def parse(self, response):
        item=collection75Item()
        item["museumID"]=14
        item['collectionName']=response.xpath("//div[@class='bodybg']/div[@class='w1200']/table/tr/td[@align='center']/text()").extract()[1]
        item['collectionImage']='www.pgm.org.cn'+response.xpath("//div[@class='bodybg']/div[@class='w1200']/table/tr/td[@width='440']/img/@src").extract_first()
        tr_list=response.xpath("//div[@class='bodybg']/div[@class='w1200']/table/tr")
        item['collectionIntroduction']=tr_list[2].xpath("./td[@style='width:40%;height:300px']/text()").extract_first()
        yield item


        









