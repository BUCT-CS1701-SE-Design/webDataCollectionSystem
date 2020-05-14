# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum4'
    allowed_domains = ['jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=4
        item["museumName"]='中国人民革命军事博物馆'
        item["Location"]='北京市海淀区复兴路9号'
        item["Link"]='http://www.jb.mil.cn/'
        item["opentime"]=response.xpath("//li[@class='header_top_link']/span/text()").extract_first()
        item["telephone"]=""
        url='http://www.jb.mil.cn/jbgk/jbjj/'
        yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list = response.xpath("//div[@class='center_wrap']/p[@class='cenText']")
        content= ''
        for p in p_list:
            x= p.xpath("./text()").extract_first()
            if x!=None:
                content+=x
        item["introduction"]=content
        yield item


