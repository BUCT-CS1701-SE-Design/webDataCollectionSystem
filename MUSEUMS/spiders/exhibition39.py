# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition39Spider(scrapy.Spider):
    name = 'exhibition39'
    allowed_domains = ['shanghaimuseum.net']
    page = 0
    urls = ['92','90','86','84','82','80','75','73','71']
    start_urls = [
        'https://www.shanghaimuseum.net/museum/frontend/display/exhibition-info-out-line-detail?exhibitionCode=E00004092']
    base_url = 'https://www.shanghaimuseum.net/museum/frontend/display/exhibition-info-out-line-detail?exhibitionCode=E000040{}'
    imagelist = [
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20200415/1586930025195_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20200110/1578621777546_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20191204/1575443819299_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20191106/1573004172420_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20191022/1571731621404_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20190923/1569212348823_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20190815/1565835555514_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20190520/1558294705325_162.jpg',
        'https://www.shanghaimuseum.net/resource/museum_files/resource_files//20190424/1556098221912_162.jpg'
    ]
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        item = exhibition75Item()
        item["museumID"] = 39
        item["exhibition_picture"] = self.imagelist[self.page]
        item["exhibitionTheme"] = response.xpath("//p[@class='f30 black']/text()").extract_first().strip()
        content = response.xpath( "//div[@class='wen']/text()").extract()
        content = content[4].strip()
        item["exhibitionIntroduction"] = content
        yield item
    # 完成每页之后开始下一页
        if self.page <= 7:
            self.page += 1
            new_url = self.base_url.format(self.urls[self.page])
            yield scrapy.Request(url=new_url, callback=self.parse)
        
