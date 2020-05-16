# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item


class Collection31Spider(scrapy.Spider):
    name = 'collection31'
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'https://baike.baidu.com/item/%E5%90%89%E6%9E%97%E7%9C%81%E8%87%AA%E7%84%B6%E5%8D%9A%E7%89%A9%E9%A6%86/7701684?fr=aladdin']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 31
        li_list = response.xpath("//div[@class='content']//table")
        for li in li_list:
            sub_list = li.xpath(".//tr")
            for sli in sub_list:
                item["collectionImage"] = 'https://baike.baidu.com' + sli.xpath(
                    "./td[position()=2]/div[@class='para']/div[@class='lemma-picture text-pic layout-right']/a/@href").extract_first().strip()
                item["collectionName"] = sli.xpath(
                    "./td[position()=2]/div[@class='para']/div[@class='lemma-picture text-pic layout-right']/span/text()").extract_first().strip()
                content = sli.xpath(
                    "./td[position()=1]/text()|./td[position()=1]/div[@class='para']/text()").extract()
                content = "".join(content).strip()
                item["collectionIntroduction"] = content
                yield item
