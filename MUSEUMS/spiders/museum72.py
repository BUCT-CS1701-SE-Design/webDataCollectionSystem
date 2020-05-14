# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }


class Museum72Spider(scrapy.Spider):
    name = 'museum72'
    allowed_domains = ['sdmuseum.com']
    start_urls = ['http://www.sdmuseum.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=72
        item["museumName"]='山东博物馆'
        item["Location"]='山东省济南市经十路11899号'
        item["telephone"]=' 0531-85058202 '
        item["Link"]='http://www.sdmuseum.com/'
        item["opentime"]='周二至周日9:00—17:00开馆，16:00停止入馆 周一（除国家法定节假日）闭馆 '
        item["introduction"]='山东省博物馆是新中国成立后建立的第一座省级综合性地志博物馆，成立于1954年。当时的馆址分为东西两院，东院位于济南市广智院街广智院旧址，系1904年英国浸礼教会牧师怀恩光创建，原是中国境内最早的博物馆之一；西院位于济南市上新街世界红万字会济南母院旧址，原是一处融道、佛、儒、基督、伊斯兰五教合一的宗教团体驻地，1942年建成。山东省博物馆成立后，将济南广智院旧址辟为自然陈列室、世界红万字会济南母院旧址辟为历史陈列室。         '
        yield item
