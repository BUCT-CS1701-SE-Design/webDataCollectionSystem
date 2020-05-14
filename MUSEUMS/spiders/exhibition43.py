# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition43Spider(scrapy.Spider):
    name = 'exhibition43'
    allowed_domains = ['cyjng.net']
    start_urls = [
        'http://www.cyjng.net/Default.aspx?tabid=264&language=zh-CN']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 43
        li_list = response.xpath("//span[@id='dnn_dnnLINKS_lblLinks']/div[position()>1]")
        for li in li_list:
            item["exhibitionTheme"] = li.xpath("./a/text()").extract_first().strip()
            url = 'http://www.cyjng.net' + li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}
            )

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        item["exhibition_picture"] = 'http://www.cyjng.net' + response.xpath("//img/@src").extract_first().strip()
        content = response.xpath("//div[@class='c_content']//div/text()|//div[@id='dnn_ctr493_HtmlModule_HtmlModule_lblContent']//p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
        
