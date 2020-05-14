# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition31Spider(scrapy.Spider):
    name = 'exhibition31'
    allowed_domains = ['museum.nenu.edu.cn']
    start_urls = [
        'http://museum.nenu.edu.cn/index.htm']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 31
        li_list = response.xpath("//div[@class='right']/div[@class='show'][position()=1]//dl")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath("./dd/text()").extract_first().strip()
            item["exhibition_picture"] = 'http://museum.nenu.edu.cn' + li.xpath("./dt/a/img/@src").extract_first().strip()
            url = 'http://museum.nenu.edu.cn/' + li.xpath("./dt/a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                #meta={"item": item}  # 传递参数
                
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath(
            "//div[@id='vsb_content']/p[position()<5]/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
