# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum17'
    allowed_domains = ['dangshi.people.com']
    start_urls = ['http://dangshi.people.com.cn/GB/151935/206880/206920/index.html#']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=17
        item["museumName"]='周恩来邓颖超纪念馆'
        item["Location"]='天津水上公园风景区'
        item["Link"]='http://dangshi.people.com.cn/GB/151935/206880/206920/index.html#'
        item["opentime"]="暂无"
        item["telephone"]="暂无"
        item["introduction"]="""周恩来邓颖超纪念馆位于天津市南开区水上公园西路，占地面积70000平方米，建筑面积12850平方米，是全国唯一一座夫妻合一的伟人纪念馆。馆区由主展厅、西花厅专题陈列厅、周恩来专机陈列厅、纪念广场等组成。1977年6月，天津市委、市政府决定在周恩来母校南开中学东楼建立周恩来同志青年时代在津革命活动纪念馆，1978年3月5日对外开放，为全国重点文物保护单位。"""
        yield item



















