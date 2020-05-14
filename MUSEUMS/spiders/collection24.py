import scrapy
from MUSEUMS.items import collection75Item
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'collection24'
    allowed_domains = ['www.nmgbwy.com']
    start_urls = ['http://www.balujun.cn/']
    def parse(self, response):
        names=['唐代铜胡人像',
               '元代阿拉伯文铜镜',
               '辽代胡人驯狮纹石雕',
               '辽代莲花形手执铜香炉',
               '蒙古族蒸酒锅']
        imgs=['http://www.nmgbwy.com/u/cms/www/201508/31161314mmyy.jpg',
              'http://www.nmgbwy.com/u/cms/www/201508/31161404h1b3.jpg',
              'http://www.nmgbwy.com/u/cms/www/201508/31161534kbv6.jpg',
              'http://www.nmgbwy.com/u/cms/www/201508/31161736ip5n.jpg',
              'http://www.nmgbwy.com/u/cms/www/201508/31161915a9lg.jpg']
        intros=['铜像造型为典型的胡人特征，体魄强健，头戴毡帽、浓眉、深目、身着铠甲，上饰具有阿拉伯风格的几何纹饰，赤足，手持武器呈射击状。',
                '铜镜上饰相互对称的两只人面兽神怪兽，外沿饰阿拉伯文，具有典型伊斯兰风格。',
                '人物造型具有典型的西域胡人特征，阔鼻大眼，身着胡服，头戴风帽。雄狮怒眼圆睁，口衔璎珞，表现出一种欲要挣脱之势，显得生动传神，很有感染力。',
                '莲花形手执铜香炉，是礼佛者行进时手持之物，莲瓣形小碗为炉身，上覆龙纹铜盖，覆莲叶做炉座，手柄末端向下弯曲，近柄处的香盒为小莲花形，专作盛香之用。这种器形最早见于北朝时期的石窟壁画中一种鹊尾柄香炉，将莲花做成香炉，出现在隋末或唐初。辽代继承唐代风格，制作精美，巧夺天工。',
                '该文物为蒙古族传统酿酒器具。蒸馏酒锅主要由大锅、小锅、蒸筒、吊罐、酒流、盛酒器、裹带等七个部分组成。']
        for i in range(5):  
            item=collection75Item()
            item["museumID"]=24
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item  







