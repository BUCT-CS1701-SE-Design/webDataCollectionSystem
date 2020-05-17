# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume122Spider(scrapy.Spider):
    name = 'musume122'
    allowed_domains = ['dtxsmuseum.com']
    start_urls = ['http://www.dtxsmuseum.com/news_show.aspx?id=832']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=122
        item["museumName"] ='大唐西市博物馆'
        item["Location"] =response.xpath('normalize-space(/html/body/div/form/div[4]/div[2]/div[2]/p[5]/span)').extract_first()
        item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='http://www.dtxsmuseum.com/'
        item["opentime"] = '全年开放（每周一及除夕闭馆，法定节假日正常开放），夏季：9：00-17：30（16：30停止票务办理），冬季：9：00-17：00（16:：0停止票务办理）'
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]=response.xpath('normalize-space(/html/body/div/form/div[4]/div[2]/div[2]/p[9]/span)').extract_first()
        item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='http://www.dtxsmuseum.com/news_show.aspx?id=1'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = response.xpath('/html/body/div/form/div[4]/div[2]/div[2]/p[11]/span/text()').extract()
        #item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        #item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
