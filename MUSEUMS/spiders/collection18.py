# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection18'
    allowed_domains = ['www.hebeimuseum.org.cn']
    start_urls = ['http://bwy.hbdjdz.com/html/goodInfo.html?id=325']
    def parse(self, response):
        names=['明赵南星书札册',
               '明万历乙未年鎗金彩漆云龙荷塘纹漆盒',
               '北齐青釉仰覆莲花尊',
               '唐白石胁侍菩萨立像',
               '清王原祁南山图轴',
               '春秋“孟姬”铜匜']
        imgs=['http://bwy.hbdjdz.com/upload_img/primary_collection/13000005-132.jpg',
              'http://bwy.hbdjdz.com/upload_img/primary_collection/13000005-6100.jpg',
              'http://bwy.hbdjdz.com/upload_img/primary_collection/13000005-86.jpg',
              'http://bwy.hbdjdz.com/upload_img/primary_collection/13000005-4153.jpg',
              'http://bwy.hbdjdz.com/upload_img/primary_collection/13000005-9743.jpg',
              'http://bwy.hbdjdz.com/upload_img/primary_collection/13000005-7626.jpg']
        intros=['尺寸：外径纵38.3厘米 横24.6厘米出土地.册页，木板封面，前题赵忠毅公书扎，纸本，行书，11开。',
                '木胎髹漆。长方形委角，子母口，长方形圈足。盖面为红色漆地，上描黑色锦纹，锦纹内鎗金卐字，主体纹饰为二龙戏珠，花纹细部以金线勾勒。盖壁四周及盒身为黑色漆地，上填红色及鎗金花纹。纹饰为湖石花卉，荷塘水鸟。委角及口沿四周饰缠枝花卉。底足四周饰鎗金云纹。内壁及盒底髹黑漆。通身有蛇腹断纹。盒底刀刻填金款识"大明万历乙未年制"。',
                '喇叭形口，长颈，丰肩，腹饱满，高足。莲瓣纹盖，盖顶正中有堆塑的覆莲捉手。颈肩之间安六个双泥条系。颈中部有三道凸起的弦纹，弦纹上部堆贴模印的团龙纹，下面堆贴兽面纹。肩部至底足装饰6层不同形态的莲瓣，肩部堆贴的两层双瓣覆莲，莲瓣圆润舒展；第三层莲瓣凸起的瓣尖恰在腹体中部，采用深雕技法刻出，棱角清晰锋利，每瓣的根部还加饰一片模印菩提树叶；第四层仰莲贴在下腹部；高足上的覆莲亦用深雕技法刻出。通体饰青釉，釉色青绿。这件器物形体高大，造型古朴，气魄宏伟，繁缛华丽，采用浅刻、深雕、模印、堆贴等多种装饰技法，具有很高的艺术水平，是北朝青瓷的代表性作品。',
                '为一立形胁侍菩萨。身姿婀娜，宽肩，挺胸，细腰斜曲，上身略向右倾，腹微鼓。胸部自左肩至右胁下斜系一条帛巾，在左胸部挽成一小结。肩披自然下垂，绕腕后在膝部作两次迴环，然后向体侧飘扬。下系长裙，颈部及腿部佩有华丽的璎珞，赤足立于仰莲座上。',
                '图轴式，纸本设色画。图中近有矾台水泊，松柏数株，山腰山角，有水阁宇舍，远有突峰漫嵌，干笔皴擦，浑厚苍润，是其杰作。右上自识“癸未嘉平为南老年道兄，五（王）之袠初度，余作南山图奉祝，偶为公事所阻。今岁往来直庐，时作时辍，日来以残腊公馀亟成之，恰值生申令辰，犹可以当补祝也。时康熙甲申腊月望后，娄东王原祁。”白文麓台朱文。',
                '匜呈椭圆形。敛口，腹微鼓，前有敞口流，后有龙形鋬，下有四蹄形足。器身上部饰阴文三角卷云纹及三角垂叶纹，纹饰洗练。鋬为龙形，龙嘴衔匜口，鼓目，竖耳，双角弯于额两侧，背刻鳞甲，背鳍与尾翼上翘。匜内底刻铭文7行38字，"惟正月初吉丁亥 蔡叔季子孙员媵孟姬有之妇沬盘。用祈囗寿，万年无疆。子子孙孙永宝用之"反映了春秋时期北方燕国与中原蔡国（今河南上蔡）互通婚嫁的密切交往。']
        for i in range(6):
            item=collection75Item()
            item["museumID"]=18
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item


        











