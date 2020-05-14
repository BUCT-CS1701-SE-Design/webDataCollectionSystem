# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }


class Museum65Spider(scrapy.Spider):
    name = 'museum65'
    allowed_domains = ['jxmuseum.cn']
    start_urls = ['http://www.jxmuseum.cn/Home/Index']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=65
        item["museumName"]='江西省博物馆'
        item["Location"]='江西省南昌市东湖区新洲路2号（人民广场南侧）'
        item["telephone"]='0791-88233369'
        item["Link"]='http://www.jgsgmbwg.com/'
        item["opentime"]=''
        item["introduction"]='江西省博物馆筹建于1953年，是全省最大的综合性博物馆，首批国家一级博物馆，全省爱国主义教育基地。60多年来，江西省博物馆历经八一广场老馆到新洲路馆到赣江北大道新馆。新馆为江西省文化中心三大馆之一，以方盒为建筑原型，寓意为宝盒，共6层，建筑面积8.6万平方米，展陈面积2.2万平方米。江西省博物馆汇集了江西各地发现的珍贵历史文物和古代艺术精品，是全省收藏文物最多的博物馆。藏品总数约为58966件（套），其中一级文物370件（套）、二级文物1063件（套）、三级文物9220件（套）、一般文物46213件（套）。藏品类别有青铜器、瓷器、书画、革命文物、杂项等，以青铜、陶瓷类文物最具特色，数量多、品位高，在全国省级博物馆中占有重要地位。特色藏品有新干大洋洲出土商代青铜器，贵溪崖墓出土东周漆木器和原始瓷器，明代藩王墓出土文物，历代陶瓷器，江西名人书画，江西近现代革命文物等。江西省博物馆确立了常设展览与临时展览相结合的陈展体系，由8个常设展览（含江西古代历史文化展、江西革命史陈列2个基本陈列，江西古代陶瓷文化展、当代景德镇陶瓷艺术名家赠品展、江西非物质文化遗产展、新干大洋洲商代遗存展、江西名人展、自然生态展6个专题展览）和3个临时展厅构成，全图景展现江西大历史格局和文化特色，高质量满足新时代公众多元需求。江西省博物馆是江西省文化新地标，兼备智能导览等公共信息化服务系统以及学术报告厅、教育活动室、文创产品展示区等公共服务功能区，正迈向高水平科研文保能力，创新服务的现代化智慧化博物馆。'
        yield item

