# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem 
import re
class Museum76Spider(scrapy.Spider):
    name = 'museum76'
    allowed_domains = ['hnzzmuseum.com']
    start_urls = ['http://www.hnzzmuseum.com/']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=76
        item["museumName"]='郑州博物馆'
        item["Link"]='http://www.hnzzmuseum.com'
        item["Location"]='郑州市嵩山南路168号'
        #item["Location"]=response.xpath("//div[@class='foot']/p[@class='foot_con']/text()").extract()[1]
        #item["telephone"]=response.xpath("//div[@class='tel_con']/p/text()").extract_first()
        item["telephone"]='团体预约电话：0371-67438090转分机8088'
        item["opentime"]='夏季：开放入馆、开始领票：09:00,停止领票、停止入场：16:00,闭馆时间：17:00;冬季：开放入馆、开始领票：09:00,停止领票、停止入场：16:00,闭馆时间：16:30'
        url='http://www.hnzzmuseum.com/about/1.html'
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        #item["introduction"]=response.xpath("//div[@class='about_box']/ul/p/text()").extract()[0]
        item["introduction"]='郑州博物馆成立于1957年7月，是一座地方综合性博物馆。原址在郑州市建设东路碧沙岗公园北伐军阵亡将士烈士祠，建于1928年8月，占地面积4330平方米。1997年，郑州市委、市政府决定兴建新馆，1999年12月28日建成并对外开放。 郑州博物馆新馆位于郑州市嵩山南路168号，占地面积14.8亩，建筑面积14200平方米。其中主展馆8337平方米，以郑州出土的商代青铜方鼎为造型基础，取"鼎立中原"之寓意，配以圆形碟状屋顶，出檐深远，线条舒展，隐喻"天圆地方"的哲学观念，建筑风格保存铜方鼎粗狂与精美相统一，是一座传统文化与时代精神巧妙融为一体的现代化建筑。'
        
        #print(item)
        yield item 

    