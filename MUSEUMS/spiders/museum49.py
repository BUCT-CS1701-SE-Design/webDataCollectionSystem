# -*- coding: utf-8 -*-
import scrapy

from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
#from scrapy.crawler import CrawlerProcess


class Museum49Spider(scrapy.Spider):
    name = 'museum49'
    allowed_domains = ['czmuseum.com']
    start_urls = ['http://www.czmuseum.com/default.php?mod=article&do=detail&tid=1']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings = {
        'ITEM_PIPELINES': {'MUSEUMS.pipelines.MuseumPipeline': 5, }
    }

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"] = 49
        item["museumName"] = '常州博物馆'
        item["Location"] = '江苏省常州市龙城大道1288号'
        item["Link"] = 'http://www.czmuseum.com'
        item["opentime"] = '9:00-17:00（16:00停止入馆）, 周一闭馆（法定节假日除外）'
        item["telephone"] = '0519-85165089、0519-85165080 转 8078'
        content = '常州博物馆创建于1958年10月，是一所集历史、艺术、自然为一体的地方综合性博物馆，为国家一级博物馆、国家4A级旅游景区。目前常州博物馆拥有藏品3万余件/套，其中国家一级文物51件（国宝级文物1件）、二级文物245件、三级文物2945件。文物藏品中的良渚玉器、春秋战国原始青瓷器、宋元的漆器与瓷器、明清书画，均为馆藏特色。常州博物馆内设有全国首家、江苏省唯一的少儿自然博物馆，拥有各类自然标本近5000种约10000件，已形成以皮毛类动物、海洋动物、国内外精品昆虫、地区性中草药、矿物晶体及古生物化石为特色的六大收藏系列，其中圣贤孔子鸟化石、翁戎螺、金斑喙凤蝶等一批化石和生物标本世界罕见，具有极高的科学价值。'
        content = "".join(content).strip()
        item["introduction"] = content
        yield item
