# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition21'
    allowed_domains = ['www.shanximuseum.com']
    start_urls = ['http://www.shanximuseum.com/temporary.html']
    def parse(self, response):
        names=['文明摇篮',
               '夏商踪迹',
               '晋国霸业',
               '民族熔炉',
               '佛风遗韵',
               '戏曲故乡',
               '明清晋商']
        imgs=['http://www.shanximuseum.com/Uploads/Picture/2019/08/14/s5d53e2be8b97c_1510_848_225_190.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2019/04/19/s5cb99aab2fec6_792_445_20_0.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2019/08/14/s5d53e3a5e27ca.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2019/08/14/s5d53e427d93f6.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2019/08/14/s5d53e467c321d.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2019/08/14/s5d53e48a8af8d.jpg',
              'http://www.shanximuseum.com/Uploads/Picture/2019/08/14/s5d53e4b6358ed.jpg',
               ]
        intros=['母亲河九曲如龙，奔流向东。在其最大最急的转弯处，有一个叫“西侯度”的小山村。180万年前，这里的人们制造出中国最早的石器工具，燃起了中国第一堆文明之火。沧海桑田，生生不息。古人类艰难的行踪踏遍了太行和吕梁之间，不灭的篝火闪亮在汾水与桑干两岸。新石器时代，先民们创造的灿烂文化，遍布山西南北。涓涓细流，百川归海；星散古国，辐辏升华。塔儿山下，尘封4500年后重见天日的城市、宫殿、文字、铜器、“礼器”、观象台和中华民族的精神图腾——龙，昭示着我们的祖先跨进文明之门。最早的“中国”人从这里出发，走向未来。',
                '公元前21世纪，中国历史进入文明时代。“父传子、家天下”的第一个王朝——夏朝建立。山西南部古有“夏墟”之称，夏文化遗存，分布密集，灿若繁星。“东下冯遗址”的发现，清楚地表明晋南是夏文化的中心区域之一。继夏而起的商朝，是中国有文字记载的历史的开端，国家体制趋于完备，文明程度更高。山西南部发现的商代早期青铜重器和完整城池，表明这里是商王朝的经略要地。商时期，山西中西部吕梁山一线属于各部族“方国”领域。这些方国与华夏民族长期交往，深受影响，文化丰富多彩而独具地域特色。时至今日，我们还无缘窥其全貌。但他们留在黄土地上时断时续的踪迹，却也清晰可辨。',
                '3000多年前，武王克商，西周建立，分封诸侯，屏藩王室。成王“桐叶封弟”，叔虞入主唐国，其子燮父改号为“晋”。其后励精图治，开疆拓土，逐渐强盛。周室东迁，文侯首功；践土会盟，文公称霸；其后纵横中原，九合诸侯，成就百年霸业。晋国鼎盛时期，地跨晋、豫、冀、鲁，疆域辽阔。春秋晚期，公室衰落，六卿专权，最终导致“三家分晋”。韩、赵、魏变法图强，称雄战国。晋国六百年伟业，奠定了山西历史文化的基石。晋南是晋国的始封地和中心区域，遗存丰厚。“曲村—天马遗址”为晋国早期都城，“晋侯墓地”震动学界。“侯马晋国遗址”是晋国晚期都城——新田，“铸铜遗址”和“侯马盟书”名扬中外。中部的“晋阳古城”则是晋国末期执掌政柄的赵简子的政治军事基地，后来成为赵国的初期都城，“赵卿大墓”气势恢宏，新人耳目。',
                '山西北通塞外草原，南临中原腹地，不仅极具军事战略价值，而且是农耕社会与草原民族交汇的前沿地带，成为华夏各民族和文化交融的“大熔炉”',
                '佛教是世界三大宗教之一。两汉之际传入中国。南北朝社会动荡，佛教成为乱世百姓的精神寄托，经帝王显贵推崇，炽烈传播，隋唐达到极盛。与之相应，佛教艺术发展迅速，辉煌迭现。佛教作为中国雕塑艺术创作的主要题材，历时漫长。石雕和彩塑佛像，金铜造像，经久不衰。',
                '中国戏曲起源于原始宗教仪式中祈福或酬神的歌舞。千百年后，由于滑稽戏和说唱等艺术形式的加盟，最终形成唱、念、做、打的综合表演形式——戏曲。同古希腊戏剧和印度梵剧一样，成为世界古代文明中的艺术瑰宝。',
                '明朝初年（14世纪），山西商人以明朝北部边塞巨大的军事需求和“开中”盐法的推行为契机，开始经营粮和盐，渐渐崛起。其后不断扩大经营地域。二三百年间，足迹遍及全中国，采取多种经营，开拓对外贸易。“晋商”称富海内，名闻天下，成为中国明清时代最重要的商帮之一。']
        for i in range(7):  
            item=exhibition75Item()
            item["museumID"]=21
            item["exhibitionTheme"]=names[i]
            item["exhibition_picture"]=imgs[i]
            item["exhibitionIntroduction"]=intros[i]
            yield item  




