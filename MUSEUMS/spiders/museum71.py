# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

class Museum71Spider(scrapy.Spider):
    name = 'museum71'
    allowed_domains = ['bowuguan.qingzhou.gov.cn']
    start_urls = ['http://bowuguan.qingzhou.gov.cn/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=71
        item["museumName"]='青州市博物馆'
        item["Location"]='山东省青州市范公亭西路1号'
        item["telephone"]='0536-3266200 '
        item["Link"]='http://bowuguan.qingzhou.gov.cn/'
        item["opentime"]='每天9：00-16：30（16：00停止入馆），每周一全天闭馆（国家法定节假日除外）'
        item["introduction"]='青州市博物馆是一座综合性博物馆，其前身益都县博物馆始建于 1959 年，原址系清康熙年间文华殿大学士冯溥的宗祠改建，1989 年迁入现址。现馆占地面积约 2.8 万平方米，建筑面积 1.2 万平方米，其整体为四合院式明清风格的仿古建筑群。2008 年被评为首批“国家一级博物馆”，2017 年与青州古城、云门山组成青州古城旅游区晋升国家 AAAAA 级旅游景区。　青州市博物馆馆藏各类文物 5 万余件，国家珍贵文物 3000 余件，其中明万历二十六年赵秉忠殿试卷填补了我国明代宫廷档案的空白，为海内外孤本；东汉“宜子孙”玉璧和战国玉人是罕见的玉器珍品；香山汉墓陪葬坑出土的彩绘陶器、陶俑是目前我国同时期同类文物中彩绘保存最好的。最著名的藏品是 1996 年龙兴寺遗址窖藏出土的 400 余尊佛教造像，时间跨越北魏至北宋，长达 500 年。这批造像数量多、品种全，雕刻精美、贴金彩绘保存完好、跨越时间长，引起海内外的高度关注，先后被评为“1996 年全国十大考古新发现”“中国 20 世纪 100 项考古大发现”，被称为改写东方艺术史的杰作。其先后多次到国内外著名博物馆举办大型专题展，成为青州走向世界的桥梁，是中国古代雕塑艺术的杰出代表，所到之处，让人叹为观止'
        yield item

