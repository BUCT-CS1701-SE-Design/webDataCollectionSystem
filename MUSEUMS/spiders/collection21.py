# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item#声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'collection21'
    allowed_domains = ['www.shanximuseum.com']
    start_urls = ['http://www.shanximuseum.com/index.html']
    def parse(self, response):
        names=['玛瑙串饰',
               '玉蟠龙',
               '傅山 户外一峰',
               '天曹府君天曹掌禄主算判官诸司判官等众',
               '释迦坐像',
               '曲德造佛三尊像龛']
        imgs=['http://www.shanximuseum.com/Uploads/Picture/2018/12/17/s5c174e30058c2.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2018/12/10/s5c0e3b8d1e364.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2018/12/14/s5c13469bb29ee.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2018/12/11/s5c0f55054c969.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2018/12/11/s5c0f5eed00cb0.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2018/12/11/s5c0f5ad307164.jpg']
        intros=['1961年侯马市上马村出土.由玉和玛瑙组成，形状有珠状、管状、片状，有的表面刻有纹饰，色泽鲜亮。',
                '2005年曲沃县羊舌墓地M2出土。表面因土沁变为黄褐色。整体造型为一条蜷曲的龙纹，双线阴刻，线条流畅。',
                '傅山（1607～1684年），字青竹、青主、侨黄等，别号甚多，尤以“朱衣道人”著名。山西阳曲人。清代著名学者、思想家、医学家、文学家、书画家。傅山的书法在17世纪的中国书坛独树一帜，他于真、草、篆、隶无不擅长，并超时代地开创了清代碑学之先河。他喜以篆、籀笔法作书，重骨力，书出颜真卿，并总结出“宁拙毋巧，宁丑毋媚，宁支离毋轻滑，宁真率毋安排”的经验。他的画作也达到了很高的艺术境界，所画山水、梅、兰、竹等均极精妙，被列入“逸品”。他的字、画均渗透出超逸的品格和崇高的气节，流溢着爱国主义的气息。所著颇多，可惜大都散佚，流传者有《霜红龛集》、《两汉书姓名韵》、《傅青主女科》等。',
                '纵117、横60厘米。画分两层。下层左方画两位高官，头戴展翅幞头，身着长袍，执圭，当系天曹府君和天曹掌禄。后有两官捧卷侍立，旁一短衣挎包随从。上层五人头戴垂翅幞头，穿长袍皂靴，当为判官，虽面目狰狞而意态自然。',
                '通高93厘米，宽45厘米。1982年山西省芮城县风陵渡出土。释迦牟尼结跏跌坐于八角形束腰须弥座上，内着袒右肩僧衣，外披袈裟，衣裙裹腿。脸型丰圆，闭目合唇，面带微笑，慈祥平和。右手残缺，左手作降魔触地印。台座下框部分刻铭文，“大唐景龙四年四月十五日弟子张敬节为七世先……帝及师僧父母法界众生同出……供养”等字。',
                '高33.5厘米，宽12厘米，厚9厘米。山西博物院旧藏。圆拱形尖楣龛，楣尖上方雕一佛二弟子像。佛作高肉髻，身着通肩大衣，双手合收于腹前，结跏跌坐于圆形台座上，二弟子面相长圆，双手亦合收腹前，盘坐于圆形台座之上。佛龛内主像作高肉髻，面相圆润，身着通肩广袖大衣，结跏跌坐于须弥台座上，双手施无畏与愿印。两侧胁侍菩萨头戴宝冠，面相长圆，一手置于腹前，一手置于身侧，下着贴体长裙，跣足立于台座上。台座下部浮雕双狮，并印刻造像记：“大唐麟德元年七月八日佛弟子曲德为亡妻赵敬造碑像一区……”']
        for i in range(6):  
            item=collection75Item()
            item["museumID"]=21
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item  




