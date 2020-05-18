# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition38Spider(scrapy.Spider):
    name = 'exhibition38'
    allowed_domains = ['dqsbwg.com']
    page = 8
    start_urls = [
        'http://www.dqsbwg.com/read.asp?fileid=8']
    base_url = 'http://www.dqsbwg.com/read.asp?fileid={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 38
        pics = response.xpath("//div[@class='ctt2']//img/@src").extract()
        if(self.page==8):
            item["exhibition_picture"] = 'http://www.dqsbwg.com/' + pics[0]
        elif(self.page==9):
            item["exhibition_picture"] = 'http://www.dqsbwg.com/' + pics[1]
        elif(self.page==10):
            item["exhibition_picture"] = 'http://www.dqsbwg.com/' + pics[2]
        item["exhibitionTheme"] = response.xpath("//td[@class='ns']//font/text()").extract_first().strip()
        item["exhibitionIntroduction"] = response.xpath(
            "//td[@class='ns']//div/text()").extract_first().strip()
        yield item

        # 完成每页之后开始下一页
        if self.page <= 9:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)
        
