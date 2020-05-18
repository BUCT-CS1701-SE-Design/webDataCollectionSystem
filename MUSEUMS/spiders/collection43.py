# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import collection75Item


class Collection43Spider(scrapy.Spider):
    name = 'collection43'
    allowed_domains = ['cyjng.net']
    start_urls = [
        'http://www.cyjng.net/Default.aspx?tabid=62&language=zh-CN']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item = collection75Item()
        item["museumID"] = 43
        li_list = response.xpath("//*[@id='dnn_ctr504_ArticleList_ctl00_lstArticles']/tr")
        for a in li_list:
            b = a.xpath("./td")
            for li in b: 
                if li.xpath(".//a/@title").extract_first() is not None:

                    item["collectionName"] = li.xpath(".//a/@title").extract_first().strip()
                    url = 'http://www.cyjng.net' + li.xpath(".//a/@href").extract_first().strip()
                     
                # 处理详情页
                    yield scrapy.Request(
                    url,
                    callback=self.parse_detail,
                    meta={'item': copy.deepcopy(item)}
                    )
                else:
                    item["collectionName"] =''
                

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]
        if  response.xpath("//img/@src").extract_first() is not None:

            item["collectionImage"] = 'http://www.cyjng.net' + response.xpath("//img/@src").extract_first().strip()
        else:
            item["collectionImage"] =''
        content = response.xpath("//p/text()|//div/text()").extract()
        
        if content is not None:
 
            content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
