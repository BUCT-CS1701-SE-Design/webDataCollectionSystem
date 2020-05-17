# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Museum54Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
    name = 'museum54'
    allowed_domains = ['chinasilkmuseum.com']
    start_urls = ['http://www.chinasilkmuseum.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=54
        item["museumName"]='中国丝绸博物馆'
        item["Location"]='浙江省杭州市西湖区玉皇山路73-1号'
        item["telephone"]='0571-87035223'
        item["Link"]='http://www.chinasilkmuseum.com/'
        item["opentime"]='9:00-17:00，16:30停止入馆，每周一9:00-12:00闭馆（法定节假日除外）'
        item["introduction"]='位于杭州西子湖畔玉皇山下的中国丝绸博物馆是国家一级博物馆，中国最大的纺织服装类专业博物馆，也是全世界最大的丝绸专业博物馆。现占地面积 42,286 平方米，建筑面积 22,999 平方米。中国丝绸博物馆于 1992 年 2月 26 日建成开放，2004 年 1 月 1 日起对公众实行免费开放。2015 年又开启了改扩建工程，经过一年的风雨兼程，2016 年 9 月国丝馆以全新的面貌呈现给国内外参观者。 经过几代丝博人的共同努力，国丝馆在征集丝绸藏品、举办国内外展览、保护纺织品文物、传承蚕桑丝织技艺、开展丝绸科普教育、弘扬丝绸文化等方面取得了令人瞩目的成绩。人类非物质文化遗产代表作“中国蚕桑丝织技艺”由此申报，“纺织品文化保护国家文物局重点科研基地”落户此地。近年来，国丝馆与世界各地的学术机构加强合作，成立了“国际丝路之绸研究联盟”，开展了大量的合作项目，正在让精美的丝绸和博大的丝绸文化，沿着丝绸之路，走向世界，走向人类的美好明天！ 博物馆工作职责：弘扬古蚕绢文化，开拓新丝绸之路。丝绸及其他纺织品和与之相关的服饰类文物、藏品的收藏、研究、展示、复制、仿制、鉴定、修复保护的技术服务，丝绸文化的宣传，教育及文化项目的开发与服务，蚕桑丝织染绣类非物质文化遗产的保护及传承，承担浙江省文化厅交办的其他事项。'
        yield item
