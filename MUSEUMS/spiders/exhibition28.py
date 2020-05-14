# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition28Spider(scrapy.Spider):
    name = 'exhibition28'
    allowed_domains = ['lvshunmuseum.org']
    start_urls = ['http://www.lvshunmuseum.org/Exhibition']
    page = 1
    base_url = 'http://www.lvshunmuseum.org/Exhibition/default.aspx?SortID=2&Page={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 28
        li_list = response.xpath("//div[@class='new_show']/ul/li")
        for li in li_list:
            image_url = li.xpath(
                "./a/div[@class='picbox']/img/@src").extract_first()
            item["exhibition_picture"] = 'http://www.lvshunmuseum.org' + \
                image_url.strip()
            url = 'http://www.lvshunmuseum.org' + \
                li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

        # 完成每页之后开始下一页
        if self.page <= 6:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath(
            "//div[@class='showcase_detail']/div[@class='textshow']/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        item["exhibitionTheme"] = response.xpath(
            "//div[@class='showcase_detail']/div[@class='ps_text']/h1/text()").extract_first()
        yield item
