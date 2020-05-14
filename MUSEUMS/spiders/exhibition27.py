# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition27Spider(scrapy.Spider):
    name = 'exhibition27'
    allowed_domains = ['918museum.org.cn']
    start_urls = [
        'http://www.918museum.org.cn/index.php/article/listarticle/pid/194/rel/thumb/sidebar/sidebar']
    page = 1
    base_url = 'http://www.918museum.org.cn/index.php/article/listarticle/pid/194/rel/thumb/sidebar/sidebar?currentPage={}'
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 27
        li_list = response.xpath("//div[@class='article row ']/div")
        for li in li_list:
            image_url = li.xpath("./a/img/@src").extract_first().strip()
            item["exhibition_picture"] = 'http://www.918museum.org.cn' + image_url
            url = 'http://www.918museum.org.cn' + \
                li.xpath("./a/@href").extract_first().strip()

            # 处理详情页
            yield scrapy.Request(
                url,
                callback=self.parse_detail,
                meta={"item": item}  # 传递参数
            )

        # 完成每页之后开始下一页
        if self.page <= 4:
            self.page += 1
            new_url = self.base_url.format(self.page)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        # 取出meta的item
        item = response.meta["item"]

        content = response.xpath(
            "//div[@class='article box']/div[@class='article_content']/p/text()|//div[@class='article_content']/div[@class='article_content']/p/text()").extract()
        content = "".join(content).strip()
        item["exhibitionIntroduction"] = content
        item["exhibitionTheme"] = response.xpath(
            "//div[@class='article_title']/text()").extract_first().strip()
        yield item
