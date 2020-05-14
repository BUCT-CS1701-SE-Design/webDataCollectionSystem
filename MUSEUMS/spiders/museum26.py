# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum26'
    allowed_domains = ['www.lnmuseum.com']
    start_urls = ['http://www.lnmuseum.com.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=26
        item["museumName"]='辽宁省博物馆'
        item["Location"]='沈阳市浑南区中心广场东北侧（浑南区智慧三街157号）'
        item["Link"]='http://www.lnmuseum.com.cn/'
        item["opentime"]="4月1日至10月31日9:00—17:00  11月1日至3月31日9:30—16：30"
        item["telephone"]="电话：024-23205102-5100"
        item["introduction"]="""辽宁省博物馆新馆位于沈阳市浑南区中心广场东北侧（浑南区智慧三街157号），占地面积83,200平方米，建筑面积100,013平方米，分陈列展览、观众服务、文物库房、文物保护、综合业务等五个业务区。此外，利用新馆序厅正面影壁和两侧各六块墙体，以辽宁历史文化为主题，创作铜质浮雕，以展现辽河流域的悠久历史与灿烂文明，并为新馆建筑增加浓厚的文化内涵。从主浮雕方向右前方顺时针排列，以主浮雕“文明曙光”为起点，依次为“北土方国”、“开疆拓土”、“华夏一统”、“开发辽东”、“儒风北渐”、“隋唐营州”、“契丹肇兴”、“金代东京”、“九边之首”、“满族崛起”、“东北易帜”、“国歌序曲”。13块浮雕以高度概括的艺术形象系统生动地展现辽河文化的发展史，也是辽博新馆序厅的特别之处，值得观众细细品味。建成开放后的辽博新馆将以创建东北最大、国内一流、国际知名国家级博物馆为发展目标，以“五个一流”即一流的设施、一流的功能、一流的管理、一流的服务、一流的展览为发展定位，努力在保护和弘扬中华民族优秀文化遗产，传播人类先进文化，满足人民群众精神文化生活，推动辽宁文化事业繁荣发展等方面发挥积极作用。"""
        yield item

