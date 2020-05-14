# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum9'
    allowed_domains = ['www.1937china.com/kzjng']
    start_urls = ['http://www.1937china.com/kzjng/views/wwsc/wwsc_jpdc.html']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=9
        item["museumName"]='中国人民抗日战争纪念馆'
        item["Location"]='北京市西南卢沟桥畔宛平城内街101号'
        item["Link"]='http://www.1937china.com/kzjng/'
        item["opentime"]="星期二至星期日,每日9:00-16:30,16:00止票,16:15静场,16:30闭馆"
        item["telephone"]="预约电话:010-63777088,010-63777188"
        item["introduction"]="""中国人民抗日战争是一场伟大的民族解放战争，是中国人民反抗日本军国主义侵略、争取民族解放、捍卫自由独立的正义战争。中国人民抗日战争是世界反法西斯战争的东方主战场，为世界反法西斯战争胜利做出了巨大贡献。中国人民抗日战争的胜利，是中国近代以来抗击外敌入侵取得的第一次完全胜利，是中华民族走向振兴的重大转折点，是中华民族历史上的光辉篇章。"""
        yield item





