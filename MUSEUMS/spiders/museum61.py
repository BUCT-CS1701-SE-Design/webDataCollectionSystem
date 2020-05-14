# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

class Museum61Spider(scrapy.Spider):
    name = 'museum61'
    allowed_domains = ['qzhjg.cn']
    start_urls = ['http://www.qzhjg.cn/html/index.html']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=61
        item["museumName"]='泉州海外交通史博物馆'
        item["Location"]='福建省泉州市丰泽区东湖街425号'
        item["telephone"]='0595-22100561'
        item["Link"]='http://www.qzhjg.cn/html/index.html'
        item["opentime"]='夏令时：上午 8：30 —下午5：30 冬令时：上午 8：30 —下午5：00 东湖街馆区：每周一闭馆（节假日除外）泉州湾古船陈列馆（开元寺内）：每逢农历26闭馆'
        item["introduction"]='泉州海外交通史博物馆（简称“泉州海交馆”）是国家一级博物馆，创建于1959年，原址位于著名佛教寺院泉州开元寺院内东侧。1991年2月，新馆主楼于东湖街落成。2003年，在主体楼东侧又建成了“泉州伊斯兰文化陈列馆”。目前，新、旧二馆总占地面积3.5万平方米，建筑面积1.73万平方米，陈列面积11000平方米。泉州海交馆是以反映古代海外交通、海上丝绸之路，以及由此引发的各种经济、文化交流为主题的博物馆。它以中世纪东方第一大港——刺桐（即Zaitun，泉州别称）港的历史为轴心，以丰富独特的海交文物，生动地再现我国古代悠久辉煌的海洋文化，讴歌中国人民勇于征服海洋的英雄气概，展示中华民族对人类开辟“海上丝绸之路”的重大贡献，以及在航海与造船技术方面的许多伟大发明。目前，我馆辟有“刺桐——古泉州的故事”、“泉州湾古船陈列馆”、“泉州宗教石刻馆”、“中国舟船世界”、“阿拉伯-波斯人在泉州陈列馆”等固定陈列及2个预约开放展览——“庄亨岱藏品馆”、“泉州海交民俗文化陈列馆”。在这些展厅中，分别陈列着不少举世闻名的文物瑰宝，除了一艘迄今国内发现年代最早、体量最大的宋代海船及其大量伴随出土物外，还有数十根木、铁、石古代锚具，数百方宋元伊斯兰教、古基督教、印度教石刻，各个时期的外销陶瓷器，160多艘中国历代各水域的代表性船模，以及数量繁多的反映海外交通民俗文化的器物。'
        yield item
