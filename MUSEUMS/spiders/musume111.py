# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musume111Spider(scrapy.Spider):
    name = 'musume111'
    allowed_domains = ['hongyan.info']
    start_urls = ['http://www.hongyan.info/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=111
        item["museumName"]='重庆红岩历史博物馆'
        item["Location"]='重庆市渝中区红岩村52号'
        item["Link"]='http://www.hongyan.info/'
        item["opentime"]='1月1日-12月31日 09:00-17:00'
        item["telephone"]='023-63300192 63303065'
        url='http://www.hongyan.info/'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]='重庆红岩联线文化发展管理中心（重庆红岩革命历史博物馆）［简称：红岩联线管理中心（红岩博物馆）］是重庆市文化和旅游发展委员会直属的全额拨款正局级事业单位，下辖红岩革命纪念馆、重庆歌乐山革命纪念馆（重庆歌乐山烈士陵园管理处）、中国民主党派历史陈列馆及其所属革命遗址群。红岩联线管理中心（红岩博物馆）藏品10万件，珍贵可移动文物3120件（套）；先后整合文物遗址53处文物遗址（本体32处、附属21处），对外免费开放33处（本体18处、附属15处），其中4批全国重点文物保护单位，1批国家级抗战纪念遗址，1批国家级烈士纪念设施，1批重庆市文物保护单位。主要职责为保护红岩革命历史文化遗址，研究发掘革命历史文化资源，宣传弘扬红岩精神，传播革命历史和科学文化知识。每年接待观众600余万人次。主要荣誉：国家一级博物馆、国家AAAA级旅游景区、全国十大红色旅游景区、全国爱国主义教育基地、全国廉政教育基地、全国统一战线传统教育基地、全国地方特色党性教育基地、全国研学旅游示范基地、全国中小学研学实践教育基地、国家国防教育示范基地、全国机要系统革命传统教育基地、全国“我最向往的党史纪念地”、全国文化体制改革先进单位、全国文明景区先进单位、全国红色旅游先进单位等。'
        #print(item)
        yield item 
