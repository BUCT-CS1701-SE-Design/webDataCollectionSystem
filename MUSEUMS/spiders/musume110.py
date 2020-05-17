# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume110Spider(scrapy.Spider):
    name = 'musume110'
    allowed_domains = ['3gmuseum.cn']
    start_urls = ['http://www.3gmuseum.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=110
        item["museumName"]='重庆中国三峡博物馆'
        item["Location"]=response.xpath("/html//div/div/div[5]/div[2]/div[2]/div/div[2]/ul/li[5]/p/text()").extract_first()
        item["Link"]='http://www.3gmuseum.cn/'
        item["opentime"]='每日9:00-17:00（16:00禁止入馆） 周一闭馆（法定节假日除外）'
        item["telephone"]=response.xpath("/html//div/div/div[5]/div[2]/div[2]/div/div[2]/ul/li[1]/p/text()").extract_first()
        url='http://www.3gmuseum.cn/web/article/toArticleNo.do?articleno=1&base=&fullPath=http%3A%2F%2Fwww.3gmuseum.cn&type=&itemsonno=12121212&topitemno=402880b25a3bb962015a3bc512212223&itemno=402880b25a3bb962015a3bc512212223'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("/html//div[2]/div[2]/div/div[3]/div/div[2]/div/p/text()").extract()
        #print(item)
        yield item 
