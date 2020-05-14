# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition33Spider(scrapy.Spider):
    name = 'exhibition33'
    allowed_domains = ['wmhg.com.cn']
    start_urls = [
        'https://www.wmhg.com.cn/permanent.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 33
        li_list = response.xpath("//div[@class='list-box clear']/div[@class='list-item']")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath(".//div[@class='h18']/a/text()").extract_first().strip()
            item["exhibition_picture"] = 'https://www.wmhg.com.cn' + li.xpath(".//div[@class='img']/a/img/@src").extract_first().strip()
            url = 'https://www.wmhg.com.cn' + li.xpath(".//div[@class='img']/a/@href").extract_first().strip()

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
            "//div[@class='text']/div[@class='p']/p/span/text()|//div[@class='text']/div[@class='p']/span/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
