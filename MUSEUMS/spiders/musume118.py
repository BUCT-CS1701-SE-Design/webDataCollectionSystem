# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume118Spider(scrapy.Spider):
    name = 'musume118'
    allowed_domains = ['beilin-museum.com']
    start_urls = ['http://www.beilin-museum.com/contents/47/4267.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=118
        item["museumName"]='西安碑林博物馆'
        item["Location"]='西安三学街15号'
        item["Link"]='http://www.beilin-museum.com/'
        content=""
        x = response.xpath("//table[4]//table[2]//td[3]/table[3]//div[3]/p[2]/text()[1]").extract_first()
        content += x
        x = response.xpath("//table[4]//table[2]//td[3]/table[3]//div[3]/p[2]/text()[2]").extract_first()
        content += x
        x = response.xpath("//table[4]//table[2]//td[3]/table[3]//div[3]/p[2]/text()[3]").extract_first()
        content += x
        item["opentime"]=content.replace(u'\xa0', u'')
        item["telephone"]='87210764'
        url='http://www.beilin-museum.com/contents/45/976.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("normalize-space(//table[4]//table[2]//td[3]/table[3]//div[3]/p[13]/text())").extract_first()
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u'')
        #print(item)
        yield item 
