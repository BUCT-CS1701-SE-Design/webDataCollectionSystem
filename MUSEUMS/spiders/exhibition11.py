# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition11'
    allowed_domains = ['www.chnmuseum.cn']
    start_urls = ['http://www.chnmuseum.cn/zl/zhanlanyugao/']
    def parse(self, response):
        li_list=response.xpath("//div[@class='cj_ercom_wai cj_huise cj_pb4577']/div[@class='cj_zlv_mar']/ul/li")
        for li in li_list:
            item=exhibition75Item()
            item["museumID"]=11
            item["exhibitionTheme"]=li.xpath("./a/img/@alt").extract_first()
            item["exhibition_picture"]='http://www.chnmuseum.cn/zl'+li.xpath("./a/img/@src").extract_first()[2:]
            url='http://www.chnmuseum.cn/zl'+li.xpath("./a/@href").extract_first()[2:]
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        p_list=response.xpath("//div[@class='zljsCBox']/p/text()").extract()
        content=""
        for p in p_list:
            content+=p
        item["exhibitionIntroduction"]=content
        yield item
       
       

        








