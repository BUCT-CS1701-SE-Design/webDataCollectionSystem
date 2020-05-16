# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import collection75Item

class Collection55Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection55'
    allowed_domains = ['nbmuseum.cn']
    start_urls = ['http://www.nbmuseum.cn/art/2016/6/27/art_581_3799.html']

    def parse(self, response):
        #d_list=response.xpath("//div[@id='1099']")
        tag=response.text
        #print(tag)
        #date = re.findall(r'<tr>(.*?)</tr>',str(tag))
        date = re.findall(r'<td  height=\'128\' align=\'center\' valign=\'top\'>(.*?)</td>',str(tag))
        #print(date)
        for d in date:
            item=collection75Item()
            item["museumID"]=55
            #print(d)
            item["collectionName"]=re.findall('<a title=\'(.*?)\'',d)
            item["collectionName"] = ''.join(item["collectionName"])
            img=re.findall('<img src=\'(.*?)\'',d)
            item["collectionImage"] ='http://www.nbmuseum.cn'+ ''.join(img)
           # print(item)
            url=re.findall('href=\'(.*?)\'',d)
            url ='http://www.nbmuseum.cn'+ ''.join(url)
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item":item},
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        content=response.xpath("//div[@id='zoom']/p/text()").extract()
        item["collectionIntroduction"]=''.join(content)
        yield item