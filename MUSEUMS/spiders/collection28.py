# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item

class Collection28Spider(scrapy.Spider):
    name = 'collection28'
    allowed_domains = ['lvshunmuseum.org']
    start_urls = ['http://www.lvshunmuseum.org/collection/product.aspx?SortID=9']
    page = 1
    base_url = 'http://www.lvshunmuseum.org/collection/product.aspx?SortID=9&Page={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item=collection75Item()
        item["museumID"]=28
        li_list = response.xpath("//div[@class='collection']/ul/li")
        for li in li_list:
            image_url = li.xpath(
                "./a/div[@class='picbox']/img/@src").extract_first()
            item["collectionImage"] = 'http://www.lvshunmuseum.org' + \
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
        if self.page <= 3:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)
                    
    def parse_detail(self,response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath(
            "//div[@class='showcase_detail']/div[@class='textshow']/p/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        item["collectionName"] = response.xpath(
            "//div[@class='showcase_detail']/div[@class='ps_text']/h1/text()").extract_first()
        yield item

