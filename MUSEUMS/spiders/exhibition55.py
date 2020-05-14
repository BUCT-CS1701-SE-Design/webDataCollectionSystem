# -*- coding: utf-8 -*-
import scrapy
import re
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition76Pipeline': 2,}
    }

class Exhibition55Spider(scrapy.Spider):
    name = 'exhibition55'
    allowed_domains = ['nbmuseum.cn']
    start_urls = ['http://www.nbmuseum.cn/col/col461/index.html']

    def parse(self, response):
        tag=response.text
        date = re.findall(r'<tr>(.*?)</tr>',str(tag))
        i=0
        for d in date:
            item=exhibition75Item()
            item["museumID"]=55
            i+=1
            content=re.findall('<td height="45" align="left" style="color:#ffffff; padding-left:8px; font-size:13px;">(.*?)</td>',d)
            item["exhibitionTime"]=''.join(content)
            

            '''if i%10==2 or i%10==7:
                url1=re.findall('href="(.*?)"',d)   
                url='http://www.nbmuseum.cn'+ ''.join(url1)
                #print(url)
                yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )'''
            url1=re.findall('href="(.*?)"',d)   
            url='http://www.nbmuseum.cn'+ ''.join(url1)
                #print(url)
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
            
    def parse_detail(self,response):
        item=response.meta["item"]
        if response.xpath("//div[@class='ad-thumbs']/ul/li/a/img/@src").extract_first() is not None:

            item["exhibition_picture"]='http://www.nbmuseum.cn'+response.xpath("//div[@class='ad-thumbs']/ul/li/a/img/@src").extract_first()
        else:
            item["exhibition_picture"]=''
        item["exhibitionTheme"]=response.xpath("//span[@class='title']/text()").extract_first()
        
        content=response.xpath("//div[@class='list_top']/p[1]/text()").extract_first()
        p_list=response.xpath("//div[@class='list_top']/p[2]/span")
        for p in p_list:
            if p.xpath("./text()").extract_first() is not None and content is not None:

                content+=p.xpath("./text()").extract_first()
        if response.xpath("//div[@class='list_top']/p[2]/text()").extract_first() is not None and content is not None:
            content+=response.xpath("//div[@class='list_top']/p[2]/text()").extract_first()
        item["exhibitionIntroduction"]=content
        yield item

            
