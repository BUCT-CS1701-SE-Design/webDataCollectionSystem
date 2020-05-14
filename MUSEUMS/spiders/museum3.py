# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum3'
    allowed_domains = ['gmc.org.cn']
    start_urls = ['http://www.gmc.org.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=3
        item["museumName"]='中国地质博物馆'
        item["Location"]='北京市西城区西四羊肉胡同15号'
        item["Link"]='http://www.gmc.org.cn/'
        time_list= response.xpath("//div[@class='list clear']/div[@class='li']")
        content=""
        for time in time_list:
            content+= time.xpath("./div[@class='p']/text()").extract_first()+": "+time.xpath("./div[@class='tiem']/text()").extract_first()

        item["opentime"]=content
        item["telephone"]=response.xpath("//div[@class='tele']/text()").extract_first()+response.xpath("//div[@class='tele']/span/text()").extract_first()
        url='http://www.gmc.org.cn/about/address.html@dbjj'
        yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list = response.xpath("//div[@class='pbox']/p")
        content= ''
        for p in p_list:
            x= p.xpath("./text()").extract_first()
            if x!=None:
                content+=x
        item["introduction"]=content
        yield item

