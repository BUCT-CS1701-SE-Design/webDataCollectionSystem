# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置

class Musume1Spider(scrapy.Spider):
    name = 'museum15'
    allowed_domains = ['www.tjbwg.com']
    start_urls = ['https://www.tjbwg.com/cn/Index.aspx']
    # 设置经过哪个pipeline去处理，必须设置
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}
    }
    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=15
        item["museumName"]='天津博物馆'
        item["Location"]='天津市河西区平江道62号'
        item["Link"]='https://www.tjbwg.com/cn/Index.aspx'
        item["opentime"]="09:00—11:00   11:00—14:00    14:00—16:00"
        item["telephone"]="电话：022-83883000"
        item["introduction"]="""天津博物馆是一座历史艺术类综合性博物馆，其前身可追溯到1918年成立的天津博物院，是国内较早建立的博物馆之一。其收藏特色是中国历代艺术品和近现代历史文献、地方史料并重，现有古代青铜器、陶瓷器、法书、绘画、玉器、玺印、文房用具、甲骨、货币、邮票、敦煌遗书、竹木牙角器、地方民间工艺品及近现代历史文献等各类藏品近20万件，图书资料20万册。2007年底对外免费开放，2008年被评为国家一级博物馆。"""
        yield item


















