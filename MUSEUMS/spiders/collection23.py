# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item#声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection23'
    allowed_domains = ['www.balujun.cn']
    start_urls = ['http://www.balujun.cn/']
    def parse(self, response):
        names=['抗战时期孙继先使用过的狗皮褥子',
               '反法西斯联盟国国旗',
               '抗战时期聂荣臻送给刘显宜的行军床',
               '山西牺盟会会员证章',
               '冀南银行行徽',
               '白晋北段破击战中民兵用过的铁扳手']
        imgs=['http://www.balujun.cn/uploadfile/2010/0519/20100519044802417.jpg',
              'http://www.balujun.cn/uploadfile/2010/0901/20100901093019886.jpg',
              'http://www.balujun.cn/uploadfile/2010/0901/20100901093143182.jpg',
              'http://www.balujun.cn/uploadfile/2010/0901/20100901094315938.jpg',
              'http://www.balujun.cn/uploadfile/2010/0901/20100901095239126.jpg',
              'http://www.balujun.cn/uploadfile/2010/0901/20100901095422667.jpg']
        intros=['抗战时期孙继先使用过的狗皮褥子',
                '反法西斯联盟国国旗',
                '抗战时期聂荣臻送给刘显宜的行军床',
                '山西牺牲救国同盟会证章：直径2.5厘米，铜质，圆形，土黄色地上绘中国地图，其中东三省用蓝色表示，其余为深绿色。上镌“牺牲救国”4个大字。',
                '冀南银行行徽：纵3.3，横3，铜质。盾形，周围双凸线框边，孔雀蓝填色，中间金色圆圈内双钩金色线填深烤蓝色英文字母：“CHB”，圈上下分别为“晋冀鲁豫边区”和“冀南银行”楷书金色阳文。',
                '白(圭)晋(城)北段破击战中民兵用过的铁扳手为铁质，黑色，长49，扳手宽13.2。']
        for i in range(6):  
            item=collection75Item()
            item["museumID"]=23
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item  






