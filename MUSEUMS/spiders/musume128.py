# -*- coding: utf-8 -*-
import os
import scrapy
import sys
sys.path.append('..')
from items import MuseumsItem #包含这个item类，必须设置


class Musume128Spider(scrapy.Spider):
    name = 'musume128'
    allowed_domains = ['baike.baidu.com']
    start_urls = ['https://baike.baidu.com/item/%E9%9D%92%E6%B5%B7%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1627225?fr=aladdin']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=128
        item["museumName"] = '青海省博物馆'
        item["Location"] = '青海省西宁市西关大街58号'
        #item["Location"] = str(item["Location"]).replace(u'\\xa0', u' ')
        #item["Location"] = str(item["Location"]).replace(u'\xa0', u' ')
        item["Link"]='http://www.qhmuseum.cn/'
        item["opentime"] = '夏季：9:00—16:30；冬季：9:30—16:00，每周一闭馆休整。'
        #item["opentime"] = str(item["opentime"]).replace(u'\\xa0', u' ')
        #item["opentime"] = str(item["opentime"]).replace(u'\xa0', u' ')
        item["telephone"]= '0971--6118691'
        #item["telephone"] = str(item["telephone"]).replace(u'\\xa0', u' ')
        #item["telephone"] = str(item["telephone"]).replace(u'\xa0', u' ')
        url='https://baike.baidu.com/item/%E9%9D%92%E6%B5%B7%E7%9C%81%E5%8D%9A%E7%89%A9%E9%A6%86/1627225?fr=aladdin'
        # 处理详情页
        
        yield scrapy.Request(
            url,
            callback=self.parse_detail,
            meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["introduction"] = '青海省博物馆位于西宁市城西区新宁广场东侧，是青海第一座具有现代化功能的大型综合博物馆，隶属于青海省文化和新闻出版厅，为省级公益一类事业单位，占地17000平方米，建筑面积20800平方米。青海省博物馆最早筹建于1957年，1986年9月正式建立并对外开放。2001年5月1日，青海省博物馆新馆建成开放，2008年4月1日起面向社会免费开放，2017年1月被中国博物馆协会评为国家一级博物馆。截至2017年12月，该馆设主、侧展厅10个，展厅面积9146平方米。文物库房7个，面积2593平方米。馆藏文物14932件/套，其中珍贵文物2193件/套。馆藏文物以新时期彩陶和民族宗教类文物最具特色，涉及宗教、民俗、政治、经济、军事、生产生活等多个领域。承担着以展览展示、文物保护、科学研究、人才队伍培养、社会服务功能、对外教育宣传及交流等多项工作。'
        item["introduction"] = str(item["introduction"]).replace(u'\\xa0', u' ')
        item["introduction"] = str(item["introduction"]).replace(u'\xa0', u' ')
        #print(item)
        yield item 
