# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum11'
    allowed_domains = ['www.chnmuseum.cn']
    start_urls = ['http://www.chnmuseum.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=11
        item["museumName"]='中国国家博物馆'
        item["Location"]='中国北京东城区东长安街16号'
        item["Link"]='http://www.chnmuseum.cn/'
        item["opentime"]="开馆时间09:00  停止入馆16:30  观众退场16:30  17:00闭馆时间"
        item["telephone"]="参观咨询热线：010-65116400（9:00-16:00）"
        item["introduction"]="""中国国家博物馆是代表国家收藏、研究、展示、阐释能够充分反映中华优秀传统文化、革命文化和社会主义先进文化代表性物证的最高机构，是国家最高历史文化艺术殿堂和文化客厅。2012年11月29日，习近平总书记率领十八届中央政治局常委来到中国国家博物馆参观“复兴之路”基本陈列，发出实现中华民族伟大复兴中国梦的伟大号召，中国特色社会主义新时代在这里扬帆启程。2018年11月13日，习近平总书记等中央领导同志来到中国国家博物馆参观“伟大的变革——庆祝改革开放40周年大型展览”，要求通过展览教育引导广大干部群众更加深刻地认识到中国共产党、中国人民和中国特色社会主义的伟大力量，更加深刻地认识到我们党的理论是正确的、党中央确定的改革开放路线方针是正确的、改革开放的一系列战略部署是正确的，更加深刻地认识到改革开放和社会主义现代化建设的光明前景，统一思想、凝聚共识、鼓舞斗志、团结奋斗，坚定跟党走中国特色社会主义道路、改革开放道路的信心和决心。"""
        yield item






