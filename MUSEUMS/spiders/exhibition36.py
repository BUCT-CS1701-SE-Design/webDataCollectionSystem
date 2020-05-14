# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition36Spider(scrapy.Spider):
    name = 'exhibition36'
    allowed_domains = ['aihuihistorymuseum.org.cn']
    start_urls = [
        'http://www.aihuihistorymuseum.org.cn/show_index.aspx?type=347']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 36
        li_list = response.xpath("//div[@class='show_two']/div[@class='show_box'][position()>2]")
        for li in li_list:
            item["exhibition_picture"] = 'http://www.aihuihistorymuseum.org.cn' + li.xpath("./a/div[@class='show_img']/img/@src").extract_first().strip()
            url = 'http://www.aihuihistorymuseum.org.cn/' + li.xpath("./a/@href").extract_first().strip()

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

        item["exhibitionTheme"] = response.xpath("//head/title/text()").extract_first().strip()
        content = response.xpath(
            "//span[@id='ContentPlaceHolder1_content']/p/span/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        yield item
