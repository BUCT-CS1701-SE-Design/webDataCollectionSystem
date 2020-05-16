# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置


class Museum70Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

    name = 'museum70'
    allowed_domains = ['jiawuzhanzheng.org']
    start_urls = ['http://www.jiawuzhanzheng.org/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=70
        item["museumName"]='中国甲午战争博物馆'
        item["Location"]='山东省威海市环翠区刘公岛'
        item["telephone"]='(0631)5324184'
        item["Link"]='http://www.jiawuzhanzheng.org/'
        item["opentime"]='淡季 8:30 — 16:30(16:00停止入场) 旺季 7:30 — 18:00 (17:30停止入场)'
        item["introduction"]='中国甲午战争博物馆，国家一级博物馆，是以北洋海军和甲午战争为主题的纪念遗址性博物馆，馆址设在刘公岛原北洋海军提督署内。该馆从1985年到现在共接待110多个国家的近千万观众，其中包括90多位党和国家领导人。1994年，中日甲午战争一百周年之际，江泽民同志为甲午战争博物馆题写了馆名。博物馆现在开放的参观景点有提督署、龙王庙、丁汝昌寓所、北洋海军将士纪念馆、水师学堂、东泓炮台、公所后炮台、旗顶山炮台，总面积达十多万平方米。目前，馆内藏有历史照片1000多幅，北洋海军与甲午战争文物资料200多件，打捞舰船文物300多件。中国甲午战争博物馆是甲午战争纪念地专门的管理、保护机构，所辖北洋海军和甲午战争的历史遗迹28处。1988年1月，刘公岛甲午战争纪念地被国务院公布为全国重点文物保护单位。博物馆以丰富的历史遗迹和特色鲜明的陈列展示，吸引着海内外的广大观众。建馆以来，这里先后被评为“全国优秀社会教育基地”、“全国青少年爱国主义教育基地”“百个爱国主义教育示范基地”。中国甲午战争博物馆以其富有特色的陈列展示，成为后人凭吊甲午故地，敬缅爱国将士，铭记历史教训，接受爱国主义教育的重要场所。千百万观众从中汲取了爱国主义精神力量，产生了巨大的社会效益。'
        yield item
