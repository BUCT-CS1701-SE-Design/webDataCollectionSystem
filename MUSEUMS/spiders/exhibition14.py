# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition14'
    allowed_domains = ['www.pgm.org.cn']
    start_urls = ['http://www.pgm.org.cn/pgm/yjj/201912/d6d3d69cc0ee43dc8a710e30c4892c6a.shtml']
    def parse(self, response):
        names  =['清代王府文化展','恭王府历史沿革展','恭王府博物馆馆史展','《红楼梦》与恭王府','神音禅韵——恭王府宗教生活展']
        imgs   =['http://www.pgm.org.cn/pgm/qdwfzzljj/201810/d95a77520ccd48309dc71541de698ca0/images/d87ba0327b744684b315c52770cf1d5e.jpg',
             'http://www.pgm.org.cn/pgm/hlmzljjf/201810/c528df40fe9449c291c290623954fac7/images/cc8815729076447e930b7071d5e33267.jpg',
             'http://www.pgm.org.cn/pgm/gwfbwgzljj/201810/27d838a1b65245e6a914cf3fb09a679b/images/862b31a5d09e4efaa6ac041feac22e5e.jpg',
             'http://www.pgm.org.cn/pgm/hlmzljj/201810/199e2cd0555d4f52bc7a483dcea21801/images/eb68f11f2b3b4865a3cfdc4cbaceff5e.jpg',
             'http://www.pgm.org.cn/pgm/sycyzljj/201810/4cf7f78dc13e44108272222488e010f2/images/44442f63028942dda374b111f521d8c8.jpg']
        intros =['展览分为三大部分，第一部分为“清代的封爵制度”，第二部分为“王府的建筑和规制”，第三部分为“身系国家的大清王公”。让观众从封爵制度、王府和王公的政治、军事、外交作用来初步了解清代王府文化。',
             '展览分为“和珅”、“恭亲王奕訢”、“私属皇室宅园”、“公共文化空间”四部分，全面介绍恭王府曾经作为和珅宅、和孝公主府、庆王府、恭王府、辅仁大学和现代文化空间的历史沿革情况。展览同时展示：天花脊檩彩绘及地面旧有金砖。葆光室正殿天花彩绘保存完整，傅彩古雅，其中脊檩部分为清中期包袱式宋锦图案苏式彩绘，是难得一见的真迹。',
             '在恭王府全面开放十周年之际，全新改版的“恭王府博物馆馆史展”与观众见面。展览在葆光室东西两个配殿分别讲述恭王府博物馆的历史进程与业务建设，让馆史展成为公众了解恭王府240年历史脉络的窗口、展示恭王府博物馆从修缮队到国家一级博物馆的40年筚路蓝缕奋斗历程的平台。',
             '《红楼梦》是中国传统文化的优秀代表，在世界文学史上占有重要地位。曹雪芹在《红楼梦》中所描绘的荣宁二府及大观园，引起了诸多读者的探索兴趣。恭王府是我国现今保存最完好的王府，与《红楼梦》渊源甚深，红学新时期以来，更成为《红楼梦》研究的重镇。一个是“名著”，一个是“名府”，二者竟有着深远而微妙的关系。展览分为“曹家与北京王府”、“《红楼梦》与恭王府”、“大观园‘原型’之谜”三大版块，通过大量翔实、有趣的文献和文物资料，向大家述说一段不寻常的历史与文学的渊源。',
             '展览通过历史资料、遗迹遗存照片和部分实物的展示，全面、客观地介绍了清代恭亲王奕䜣时期，恭王府内的宗教活动情况，包括府主人对萨满教、佛教及其他宗教的信仰和膜拜。']
        for i in range(5):
            item=exhibition75Item()
            item["museumID"]=14
            item["exhibitionTheme"]=names[i]
            item["exhibition_picture"]=imgs[i]
            item["exhibitionIntroduction"]=intros[i]
            yield item     
       

        











