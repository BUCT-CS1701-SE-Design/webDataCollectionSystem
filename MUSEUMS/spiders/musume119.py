# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置

class Musum119Spider(scrapy.Spider):
    name = 'musume119'
    allowed_domains = ['banpomuseum.com.cn']
    start_urls = ['http://www.banpomuseum.com.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=119
        item["museumName"]='西安半坡博物馆'
        item["Location"]='西安市半坡路155号'
        item["Link"]='http://www.banpomuseum.com.cn/'
        item["opentime"]='旺季：（3月1日-11月30日）8:00----17:30  淡季：（12月1日-2月底）8:00----17:00'
        item["telephone"]='联系电话：029-62815385 投诉电话：18729251954'
        url='http://www.banpomuseum.com.cn/'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"]='西安半坡博物馆是新中国第一座史前聚落遗址博物馆。半坡遗址1953年春被发现，遗址面积约50000平方米。1954～1957年，中国科学院考古研究所先后进行了5次大规模的发掘，发掘面积达10000平方米。该遗址揭示了距今大约6000多年前的一处典型的新石器时代仰韶文化母系氏族聚落的社会组织、生产生活、经济形态、婚姻状况、风俗习惯、文化艺术等丰富的文化内涵。西安半坡博物馆于1958年4月建成并正式对外开放，50余年来，共计接待中外游客3000余万人次。老一辈党和国家领导人刘少奇、朱德、周恩来、邓小平等前来参观，给予了高度评价。1961年半坡遗址被国务院公布为第一批全国重点文物保护单位；1997年，西安半坡博物馆被中宣部确定为首批“百个爱国主义教育示范基地”；1998年被西安市政府评定为 “西安旅游十大景点”之一；2006年被旅游网在网上调查评为“中国最值得外国人去的50个地方”之一；2008年被中共西安市委、市政府授予“文明单位”；2008年5月被国家文物局评定为“国家一级博物馆”。西安半坡博物馆位于西安东郊浐河东岸，占地面积107.4亩。馆藏各类文物18000余件，其中三级以上文物4000多件，化石标本300余件，新石器时代的人类和动物骨骼标本若干。人面鱼纹盆是半坡遗址出土文物中最为宝贵的文物，属国家一级文物。2008年，中国人百年期盼的北京奥运会吉祥物福娃的创意灵感就来源于它。'
        #print(item)
        yield item 
