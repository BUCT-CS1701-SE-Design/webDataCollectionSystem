# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition23'
    allowed_domains = ['www.balujun.cn']
    start_urls = ['http://www.coalmus.org.cn/html/list_1612.html']
    def parse(self, response):
        names=['八路军抗战史陈列馆',
               '八路军将领馆',
               '临时展馆',
               '半景画馆']
        imgs=['http://www.balujun.cn/skin/yunhan/images/jbcl-xt.jpg',
              'http://www.balujun.cn/skin/yunhan/images/jlg-1.jpg',
              'http://www.balujun.cn/skin/yunhan/images/lszl-1.jpg',
              'http://www.balujun.cn/uploadfile/2010/0527/20100527094316814.jpg'
               ]
        intros=['八路军抗战史陈列馆是纪念馆的标志性建筑，坐北朝南，沿纪念馆中轴线向东西两侧展开，建筑风格极富民族气质，古朴庄重、雄伟壮观，展览面积8000平方米，是目前中国唯一一座全面再现八路军八年抗战历史的大型主题展馆。陈列馆主要包括序厅和6 大陈列厅，以及长达80 米的抗战文化墙长廊，还有可供观众休闲、体验虚拟抠像拍照的休息厅，具有会务接待功能的贵宾厅。',
                '国内单体展陈面积最大、展出人物最多的将领专题陈列馆。将领馆建筑面积2500余平方米，展陈面积2000平方米，是纪念馆重要的固定参观设施。主体建筑2005年建成，2011年《八路军将领馆》专题陈列初步完成布展并对外开放，2017年进行了提升改造。全面展示了1070位正旅级以上八路军将领的的光辉业绩和英雄风采，是目前国内展示人物多、规格高、内容丰富的八路军将领专题陈列。',
                '临时展馆位于八路军研究中心北侧，展馆面积约1000平方米，本着围绕中心、服务大局的宗旨，配合各个时期党和国家宣传思想文化工作需要，为满足社会公众精神文化需求，策划制作反映中国人民抗日战争伟大历史有关的专题性临时展览，也承接国内其他纪念馆的专题巡回展览。',
                '百团大战半景画馆位于抗战史陈列馆东面，二者紧紧相连，融为一体。该馆在国内首次以半景画的形式，运用声、光、电等多媒体手段，全景式再现了抗战时期八路军百团大战的恢宏气势与壮烈情景。']
        for i in range(4):  
            item=exhibition75Item()
            item["museumID"]=23
            item["exhibitionTheme"]=names[i]
            item["exhibition_picture"]=imgs[i]
            item["exhibitionIntroduction"]=intros[i]
            yield item  






