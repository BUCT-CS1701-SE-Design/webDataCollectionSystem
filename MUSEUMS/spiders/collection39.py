# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item

class Collection39Spider(scrapy.Spider):
    name = 'collection39'
    allowed_domains = ['shanghaimuseum.net']
    start_urls = ['https://www.shanghaimuseum.net/museum/frontend/articles/CI00004587.html']
    page = 0
    urls = ['87','85','83','81','79','77','75','73','71']
    base_url = 'https://www.shanghaimuseum.net/museum/frontend/articles/CI000045{}.html'
    imagelist = [
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844500086_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844354539_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844307414_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844260726_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844220023_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844186195_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844138273_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844091789_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files/20200414/1586844047773_162.jpg'
    ]

    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.CollectionPipeline':4}
    }

    def parse(self, response):
        item=collection75Item()
        item["museumID"] = 39
        item["collectionImage"] = self.imagelist[self.page]
        item["collectionName"] = response.xpath("//div[@class='cp-info-name']/text()").extract_first().strip()
        content = response.xpath( "//div[@class='cp-info-description']/text()").extract()
        content = "".join(content).strip()
        item["collectionIntroduction"] = content
        yield item
    # 完成每页之后开始下一页
        if self.page <= 7:
            self.page += 1
            new_url = self.base_url.format(self.urls[self.page])
            yield scrapy.Request(url=new_url, callback=self.parse)


