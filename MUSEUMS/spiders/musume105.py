# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume105Spider(scrapy.Spider):
    name = 'musume105'
    allowed_domains = ['jinshasitemuseum.com']
    start_urls = ['http://www.jinshasitemuseum.com/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=105
        item["museumName"]='成都金沙遗址博物馆'
        item["Location"]='四川省成都市青羊区金沙遗址路2号'
        item["Link"]='http://www.jinshasitemuseum.com/'
        item["opentime"]='夏令时8:30-20:00；冬令时8:30-18:30；周一闭馆'#response.xpath("/html/body/div[1]/section/footer/div[1]/div/text()[2]").extract_first()
        item["telephone"]=response.xpath("/html/body/div[4]/div[1]/div[1]/div/a[5]/text()").extract_first()
        url='http://www.jinshasitemuseum.com/About/Introduction'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]=response.xpath("/html/body/div[3]/div/div[2]/div/div[2]/p/text()").extract()
        #print(item)
        yield item 
