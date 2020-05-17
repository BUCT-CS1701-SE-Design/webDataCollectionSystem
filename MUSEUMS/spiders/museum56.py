# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import MuseumsItem #包含这个item类，必须设置


class Museum56Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 5,}
    }

    name = 'museum56'
    allowed_domains = ['hzmuseum.com']
    start_urls = ['http://hzmuseum.com/']

    def parse(self, response):
        item=MuseumsItem()
        item["museumID"]=56
        item["museumName"]='杭州博物馆'
        item["Location"]='浙江省杭州粮道山18号'
        item["telephone"]='0571-87802660'
        item["Link"]='http://hzmuseum.com/'
        item["opentime"]='每周二至周日9:30-16:30（16：00停止入场），周一闭馆（除国定假日外）。'
        item["introduction"]='杭州博物馆是一座展现杭州历史变迁和城市文物珍藏的人文类综合性博物馆，是浙江省最具影响力的博物馆之一，也是杭州市博物馆群体中馆藏、展陈和文化活动水平位居前列的骨干博物馆。场馆前身为2001年10月开放的杭州历史博物馆，经过多年积累与发展，已成为文物丰富、区位便捷、展览精美、设施优良的杭州历史文化亮丽窗口。杭州博物馆坐落于杭州西湖风景名胜区吴山，与吴山广场和河坊街历史文化街区相邻，占地面积2.4万平方米，建筑面积1.3万平方米，展区面积7千平方米。馆藏规模逾万件，涵盖了陶瓷、书画、玉石、印章、钱币、邮票等各类文物。镇馆之宝战国水晶杯，2002年已被国家文物局列入64件（组）首批禁止出国（境）展览的珍贵文物名录。展馆分《珍藏杭州—馆藏文物精品陈列》、《最忆是杭州—杭州历史文化陈列》和机动展厅三大部分。《珍藏杭州》系列展览展出了杭州历年来出土文物精品、杭州不可移动文物、馆藏书画精品、馆藏文房雅玩珍品、馆藏邮票等专题。《最忆是杭州》展览与杭州八千年的深厚底蕴相得益彰，在史料、史证、史人、史事的基础上，以历史朝代为串线，讲述杭州的发展历程。目前正在进行陈列改造，将于2015年十一期间对公众开放。 自2012年起，杭州博物馆每年的观众参观流量逾百万人次，2017年，正式成为是国家一级博物馆、浙江省爱国主义教育基地和杭州市文明示范博物馆，已经具备良好的社会影响力和观众美誉度。'
        yield item

