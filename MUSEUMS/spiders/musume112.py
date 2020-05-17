# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume112Spider(scrapy.Spider):
    name = 'musume112'
    allowed_domains = ['cmnh.org.cn']
    start_urls = ['https://www.cmnh.org.cn/#section1']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=112
        item["museumName"]='重庆自然博物馆'
        item["Location"]=response.xpath('normalize-space(//div[3]/div[5]//div[3]/div[1]/text())').extract_first()

        item["Link"]='https://www.cmnh.org.cn/'
        item["opentime"] = response.xpath('//div[3]/div[1]//div[3]//div[1]/p[1]/text()[3]').extract_first()
        item["telephone"]=response.xpath('normalize-space(//div/div[3]/div[5]//div[3]/h3)').extract_first()
        url='https://www.cmnh.org.cn/about/?4.html'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("normalize-space(/html/body/div[2]/div[3]/div/div/p/span/text())").extract_first()
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
