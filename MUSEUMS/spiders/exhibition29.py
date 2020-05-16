# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition29Spider(scrapy.Spider):
    name = 'exhibition29'
    allowed_domains = ['sypm.org.cn']
    start_urls = [
        'http://www.sypm.org.cn/products_list2/pmcId=54&pageNo_FrontProducts_list01-0041=1&pageSize_FrontProducts_list01-0041=16.html']
    page = 1
    base_url = 'http://www.sypm.org.cn/products_list2/pmcId=54&pageNo_FrontProducts_list01-0041={}&pageSize_FrontProducts_list01-0041=16.html'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }
    
    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 29
        li_list = response.xpath("//ul[@class='mainul productlist-02']//li[@class='content column-num4']")
        for li in li_list:
            image_url = li.xpath("./div[@class='pic-module']/div[@class='pic']/a/img/@src").extract_first().strip()
            item["exhibition_picture"] = 'http://www.sypm.org.cn' + image_url
            url = 'http://www.sypm.org.cn' + \
                li.xpath("./div[@class='pic-module']/div[@class='pic']/a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={'item': copy.deepcopy(item)}  # 传递参数
            )

        # 完成每页之后开始下一页
        if self.page <= 1:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        name = response.xpath("//li[@class='name1']/text()").extract()
        name = "".join(name).strip()
        item["exhibitionTheme"] = name
        content = response.xpath(
            "//div[@class='FrontProducts_detail02-0011_htmlbreak']//div/text()|//div[@class='FrontProducts_detail02-0011_htmlbreak']//p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
