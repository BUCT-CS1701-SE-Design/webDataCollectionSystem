# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline

class Collection75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection15'
    allowed_domains = ['tjbwg.com']
    start_urls = ['https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2673',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2672',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2668',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2667',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2632',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2631',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2630',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2550',
                  'https://www.tjbwg.com/cn/collectionInfo.aspx?Id=2538']
    def parse(self, response):
        item=collection75Item()
        item["museumID"]=15
        name_list=response.xpath("//div[@class='collD_h']/h3/text()").extract_first()
        item['collectionName']=name_list.replace(" ","")    
        item['collectionImage']=response.xpath("//div[@class='collD clearfix']/div[@class='imgList_cd']/div[@class='imgList_in']/ul/li/img/@src").extract_first()
        item['collectionIntroduction']=''
        li=response.xpath("//div[@class='d_con']/p/text()").extract_first()
        item['collectionIntroduction']=li
        yield item
        # for i in li:
            # item['collectionIntroduction']+=i
       #if item['collectionIntroduction']!='':
            #print(item) 


        









