# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition32Spider(scrapy.Spider):
    name = 'exhibition32'
    allowed_domains = ['jlmuseum.org']
    start_urls = ['http://www.jlmuseum.org/display']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 32
        li_list = response.xpath("//ul[@class='pic-list']//li")
        for li in li_list:
            image_url = li.xpath("./a/img/@src").extract_first().strip()
            item["exhibition_picture"] = 'http://www.jlmuseum.org' + image_url
            url = 'http://www.jlmuseum.org' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]
        item["exhibitionTheme"] = response.xpath("//div[@class='content']/h1/text()").extract_first().strip()
        content = response.xpath(
            "//div[@class='content']//div[@class='pics-cont']/p/text()|//div[@class='content']//div[@class='pics-cont']/p/span/text()").getall()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
