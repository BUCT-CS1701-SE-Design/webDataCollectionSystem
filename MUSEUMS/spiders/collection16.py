# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection16'
    allowed_domains = ['www.tjnhm.com']
    start_urls = ['https://www.tjnhm.com/index.php?p=kxyj_show&id=1885',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=1882',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=1872',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=1868',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=1832',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=1578',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=755',
                  'https://www.tjnhm.com/index.php?p=kxyj_show&id=860']
    def parse(self, response):
        item=collection75Item()
        item["museumID"]=16
        item['collectionName']=response.xpath("//div[@id='aboutus_text']/h1/text()").extract_first()
        img=response.xpath("//img[@alt='']/@src").extract()
        item['collectionImage']='www.tjnhm.com/'+img[0]
        p_list=response.xpath("//p/span[@style='font-family:NSimSun;font-size:16px;']")
        content=""
        for p in p_list:
            x = p.xpath("./text()").extract_first()
            if x!=None:
                content+=x
        item['collectionIntroduction']=content
        yield item


        










