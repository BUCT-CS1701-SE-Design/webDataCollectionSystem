# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection36Spider(scrapy.Spider):
    name = 'collection36'
    allowed_domains = ['aihuihistorymuseum.org.cn']
    start_urls = [
        'http://www.aihuihistorymuseum.org.cn/imglist.aspx?type=377']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 36
        li_list = response.xpath("//div[@class='sub_lcon']/div[@class='img_box']")
        for li in li_list:
            image_url = li.xpath("./a/div[@class='imgbg']/img/@src").extract_first().strip()
            item["collectionImage"] = 'http://www.aihuihistorymuseum.org.cn' + image_url
            url = 'http://www.aihuihistorymuseum.org.cn/' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["collectionName"] = response.xpath("//span[@id='ContentPlaceHolder1_content']/p/span/text()").extract_first().strip()
        content = response.xpath(
             "//span[@id='ContentPlaceHolder1_content']/p[position()>3]/span/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
