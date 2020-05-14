# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection19'
    allowed_domains = ['www.xbpjng.cn']
    start_urls = ['http://bwy.hbdjdz.com/html/goodInfo.html?id=325']
    def parse(self, response):
        names=['毛泽东用过的办公桌',
               '刘少奇用过的文件箱',
               '朱德用过的金属桌椅',
               '董必武用过的百寿杖',
               '董必武用过的棕色毛毯',
               '毛泽东用过的转椅']
        imgs=['https://bkimg.cdn.bcebos.com/pic/43a7d933c895d143afbd303d7bf082025baf07e0?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/d009b3de9c82d1581d2ea3af880a19d8bc3e4204?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/6609c93d70cf3bc775f936f2d900baa1cd112a37?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/c75c10385343fbf23ce75e3db87eca8064388fe1?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/3ac79f3df8dcd1005e6e1a3f7a8b4710b9122f3a?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/ac6eddc451da81cbcf9a6dd35a66d016092431b4?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1']
        intros=['在这张办公桌上，毛泽东同志起草了三大战役期间的许多电报手稿，起草了1948年9月政治局扩大会议的决议，撰写了《在中国共产党第七届中央委员会第二次全体会议上的报告》等许多光辉著作。',
                '刘少奇同志在延安时就开始使用这个木箱，后来把它带到西柏坡，曾用它放过《论共产党员的修养》、《关于土地问题的指示》、《中国土地法大纲》等重要文件和手稿。',
                '这套金属桌椅是在孟良固战役中缴获敌七十四师师长张灵甫的物品，朱德到前线视察时，由陈毅同志送给朱德。七届二中全会期间，陈毅、彭德怀、贺龙、邓小平等军事组的同志们就围坐在这套金属桌椅旁，讨论军事战略和作战方针。',
                '这根拐杖本来是国民党将领宋席儒送给岳父六十大寿的贺礼，淮海战役时被缴获。拐杖身部错银镶嵌篆书“寿”字四行，每行25字，共100字，字型各异，故称“百寿杖”。',
                '该毛毯长230厘米，宽165厘米，四周有两条黑色条纹，上有两处破损。是延安大生产时织的1977年6月，张连英将毛毯赠给西柏坡纪念馆。1997年5月23日，这条毛毯被国家文物局革命文物鉴定组鉴定为国家一级文物。',
                '该转椅长67.5厘米，宽58厘米，高76厘米，一腿四足，木结构圈椅式，坐面、靠背、扶手用黑色漆布包面。这把转椅是在解放后的石家庄运到西柏坡的，毛泽东就是坐在这把转椅上撰写文章、著作，批阅文件。1997年5月23日，这把皮转椅被国家文物局革命文物鉴定组鉴定为国家一级文物。']
        for i in range(6):
            item=collection75Item()
            item["museumID"]=19
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item
