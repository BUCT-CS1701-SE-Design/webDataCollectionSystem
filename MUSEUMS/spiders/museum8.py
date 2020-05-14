# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum8'
    allowed_domains = ['bmnh.org.cn']
    start_urls = ['http://www.bmnh.org.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=8
        item["museumName"]='北京自然博物馆'
        item["Location"]='北京市东城区天桥南大街126号'
        item["Link"]='http://www.bmnh.org.cn/'
        item["opentime"]="因特殊时期,具体开馆时间另行公告"
        item["telephone"]="电话：010-67024431"
        item["introduction"]="""北京自然博物馆位于首都南城中轴线上的天桥地区，背靠世界文化遗产天坛公园，面对现代化的天桥演艺区, 具有特殊的文化环境。她的前身是成立于1951年4月的中央自然博物馆筹备处，1962年正式命名为北京自然博物馆。北京自然博物馆是新中国依靠自己的力量筹建的第一座大型自然历史博物馆，主要从事古生物、动物、植物和人类学等领域的标本收藏、科学研究和科学普及工作。本馆曾先后被中央宣传部和北京市政府命名为“全国科普教育基地”和“北京市科普教育、研发、传媒基地”，被联合国教科文组织中国组委会命名为“科学与和平教育基地”，2008年被国家文物局评定为国家一级博物馆。"""
        yield item




