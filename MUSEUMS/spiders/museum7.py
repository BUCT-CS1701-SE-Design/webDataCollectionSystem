# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum7'
    allowed_domains = ['capitalmuseum.org.cn']
    start_urls = ['http://www.capitalmuseum.org.cn/']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=7
        item["museumName"]='首都博物馆'
        item["Location"]='北京市西城区复兴门外大街16号'
        item["Link"]='http://www.capitalmuseum.org.cn/'
        item["opentime"]="开放时间：09:00—17:00(16:00停止入馆，周一闭馆)"
        item["telephone"]="预约电话：010-63393339 咨询电话：010-63370491/63370492"
        item["introduction"]="""首都博物馆于1953年开始筹备，1981年正式对外开放，原馆址在全国重点文物保护单位——北京孔庙。作为北京市“十五”期间重点文化建设工程，首都博物馆新馆建设项目的立项申请，于1999年得到北京市委、市政府批准，2001年经国家发改委报国务院批准实施，2001年12月正式奠基兴建。
        首都博物馆新馆于2005年12月开始试运行，2006年5月18日正式开馆。首都博物馆以其宏大的建筑、丰富的展览、先进的技术、完善的功能，成为一座与北京“历史文化名城”、“文化中心” 和“国际化大都市”地位相称的大型现代化博物馆，并跻身于“国内一流，国际先进”的博物馆行列。"""
        yield item



