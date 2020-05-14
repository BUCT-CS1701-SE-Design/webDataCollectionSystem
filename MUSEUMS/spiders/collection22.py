# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item#声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'collection22'
    allowed_domains = ['www.coalmus.org.cn']
    start_urls = ['http://www.coalmus.org.cn/']
    def parse(self, response):
        names=['瘦煤',
               '贫煤',
               '弱黏结煤',
               '薄片透光',
               '焦煤',
               '长焰煤']
        imgs=['http://www.coalmus.org.cn/UploadFiles/2016-01/20074231150894352.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742317485376070.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742311525667786.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742022484179650.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742022455763503.jpg',
              'http://www.coalmus.org.cn/UploadFiles/2016-01/200742317422175699.jpg']
        intros=['瘦煤是炼焦用煤之中配煤，性能与焦煤相近。瘦煤焦炭块度大、裂纹少，但熔融性和耐磨性差，其用途除作炼焦配煤外，还可以用于造气、发电和其他动力用煤。',
                '贫煤是变质程度最高的烟煤，无黏结性。燃烧时火焰短，延续时间长。主要用作动力煤，也可造气，用作合成氨原料和气体燃料。',
                '弱黏结煤是炼焦煤与非炼焦煤之间的过渡煤种，主要用作造气、燃料和配焦。低硫、低灰、低磷的弱黏结煤，是全国最主要的优质动力煤。',
                '焦煤是炼焦用煤中的主焦煤，变质程度中等，结焦性和黏结性最佳。利用焦煤炼焦，可得到焦炭、焦油和焦炉气。焦炭除供给)台炼外，还可造气和电石。而焦油和焦炉气可作为燃料，还能提炼数十种化工产品。',
                '肥煤是炼焦用煤的一种，用肥煤炼出的焦炭横裂纹多，焦根部蜂焦多，易碎，但肥煤的黏结力很强，能与黏结力弱的煤搭配后炼出优质焦煤，故称肥煤为”配焦煤之母”。',
                '长焰煤是变质程度最低的煤，无黏结性和结焦性。主要用作燃料。经低温干馏可制半焦、煤气、焦油，造气后可制合成氨等。']
        for i in range(6):  
            item=collection75Item()
            item["museumID"]=22
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item  





