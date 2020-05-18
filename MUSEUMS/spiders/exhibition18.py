# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition18'
    allowed_domains = ['www.hebeimuseum.org.cn']
    start_urls = ['http://www.hebeimuseum.org.cn/contents/186/978.html',
                  'http://www.hebeimuseum.org.cn/contents/190/979.html',
                  'http://www.hebeimuseum.org.cn/contents/194/980.html',
                  'http://www.hebeimuseum.org.cn/contents/158/791.html',
                  'http://www.hebeimuseum.org.cn/contents/154/790.html',
                  'http://www.hebeimuseum.org.cn/contents/146/788.html',
                  'http://www.hebeimuseum.org.cn/contents/142/787.html',
                  'http://www.hebeimuseum.org.cn/contents/150/789.html',
                  'http://www.hebeimuseum.org.cn/contents/504/4964.html']
    def parse(self, response):
            item=exhibition75Item()
            item["museumID"]=18
            item["exhibitionTheme"]=response.xpath("//div[@class='k-d']/h3/text()").extract_first()
            li_list=response.xpath("//div[@id='focus']/ul/li")
            item["exhibition_picture"]='www.hebeimuseum.org.cn'+li_list[0].xpath("./img/@src").extract_first()
            p_list=response.xpath("//div[@class='k-d']/div[@class='text']/p/text()").extract()
            content=""
            for p in p_list:
                content+=p
            item["exhibitionIntroduction"]=content
            yield item  


