# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition51Spider(scrapy.Spider):
    name = 'exhibition51'
    allowed_domains = ['zhejiangmuseum.com']
    start_urls = ['http://www.zhejiangmuseum.com/zjbwg/exhibition/exhreview.html?retdate=2020']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 51
        li_list = response.xpath("//ul[@class='zanlan_list']/li")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath(".//a/text()").extract()[1].strip()
            item["exhibition_picture"] = 'http://www.zhejiangmuseum.com' + li.xpath(".//img/@src").extract_first().strip()
            url = 'http://www.zhejiangmuseum.com/zjbwg/exhibition/' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath("//div[@class='zanlan_zs anchor']//span/text()|//div[@class='zanlan_zs']//span/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
