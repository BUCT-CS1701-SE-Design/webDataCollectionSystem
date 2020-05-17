# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume107Spider(scrapy.Spider):
    name = 'musume107'
    allowed_domains = ['zunyihy.cn']
    start_urls = ['http://www.zunyihy.cn/guide.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item = MuseumsItem()
        item["museumID"] = 107
        item["museumName"] = '遵义会议纪念馆'
        item["Location"] = response.xpath('/html//div[4]/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/text()').extract_first()
        item["Location"] = str(item["Location"]).replace(u'\\xa0', u'')
        item["Location"] = str(item["Location"]).replace(u'\xa0', u'')
        item["Link"] = 'http://www.zunyihy.cn/'
        item["opentime"] = response.xpath('normalize-space(/html//div[4]/div[2]/div/div[1]/div/div[2]/div[2])').extract_first()
        item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u'')
        item["opentime"] = str(item["opentime"]).replace(u'\xa0', u'')
        item["telephone"] = response.xpath('/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div[3]/div[3]/text()').extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u'')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u'')
        url = 'http://www.zunyihy.cn/about.html#about2'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("normalize-space(/html/body/div[4]/div[2]/div[2]/div[2]/div/div[2]/div/div/div/text())").extract()
        #print(item)
        yield item 
