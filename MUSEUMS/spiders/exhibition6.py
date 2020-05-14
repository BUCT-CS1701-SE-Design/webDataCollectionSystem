# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition6'
    allowed_domains = ['luxunmuseum.com.cn']
    start_urls = ['http://www.luxunmuseum.com.cn/zhanlanhuigu/']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='content_zhanl']/div[@class='list_chenlie']")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=6
            item["exhibition_picture"]='http://www.luxunmuseum.com.cn'+li.xpath("./div[@class='list_img']/a/img/@src").extract_first()
            url='http://www.luxunmuseum.com.cn'+li.xpath("./div[@class='list_cl r']/dt/div[@class='more r']/a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
             
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionIntroduction"]=response.xpath("//div[@class='main_content']/div[@class='content_nr']/p/text()").extract_first()
        item["exhibitionTheme"]=response.xpath("//title/text()").extract_first()
        if item["exhibitionIntroduction"]!=None:
         yield item

        



