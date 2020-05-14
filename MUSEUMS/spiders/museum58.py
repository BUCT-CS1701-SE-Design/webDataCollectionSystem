# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }


class Museum58Spider(scrapy.Spider):
    name = 'museum58'
    allowed_domains = ['hzwhbwg.com']
    start_urls = ['http://hzwhbwg.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=58
        item["museumName"]='安徽中国徽州文化博物馆'
        item["Location"]='安徽省黄山市机场迎宾大道50号'
        item["telephone"]='0559-2574222 '
        item["Link"]='http://www.hzwhbwg.com/'
        item["opentime"]='09:00-11:30 13:30-17:00'
        item["introduction"]='安徽中国徽州文化博物馆沿革于黄山市博物馆，新馆2008年1月8日正式开馆，同年全面免费开放。位于黄山市屯溪迎宾大道50号，馆藏文物近10万余件。徽墨、歙砚、新安书画、徽州文献、徽州三雕是馆内的特色藏品。安徽中国徽州文化博物馆是国家一级博物馆、第二批全国重点古籍保护单位、安徽省青少年维权岗以及省、市两级爱国主义教育基地。安徽中国徽州文化博物馆的基本陈列为《徽州人与徽州文化》，分为：走进徽州、天下徽商、礼仪徽州、徽州建筑、徽州艺术、徽州科技六个部分。展示内容有：新安大好山水、徽州与徽州人、明清徽商、徽州女人、东南邹鲁、程朱阙里、徽州宗族、新安医学、科技之星、文房瑰宝、新安画派、徽派版画、徽派篆刻、徽州村落、徽州民居、徽州三雕等。'
        yield item

