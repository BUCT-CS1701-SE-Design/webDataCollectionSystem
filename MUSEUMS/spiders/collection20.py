# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection20'
    allowed_domains = ['www.hdmuseum.org/index.asp']
    start_urls = ['http://www.hdmuseum.org/index.asp']
    def parse(self, response):
        names=['青铜马',
               '蜀西工”造金银涂乘舆大爵酒樽',
               '酒海',
               '文字缸']
        imgs=['https://bkimg.cdn.bcebos.com/pic/5882b2b7d0a20cf4d1ba429e7e094b36acaf994d?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/9f2f070828381f3061be32e8a1014c086f06f0c8?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/e824b899a9014c0802b5b709027b02087af4f494?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
              'https://bkimg.cdn.bcebos.com/pic/aec379310a55b319aed019d94ba98226cffc1774?x-bce-process=image/resize,m_lfit,w_220,h_220,limit_1',
               ]
        intros=['在博物馆二楼的《赵文化展厅》中，陈列着我国最早、最具有写实艺术风格的三匹青铜马。其中的一匹作昂头行走状，高18厘米、长24.5厘米，五官及额鬃清晰，右腿前抬，体态劲健有力；另一匹为低头立马，高15厘米、长23.5厘米，五官及额鬃清晰，腹部铸有生殖器表示该马为雄性，马做打鼻状，生动而富有生活气息；还有一匹是后坐式立马，作低头觅食状，高15厘米，长22.5厘米，低头左倾，后足略蹲，左腿断，尾部打结下垂，五官清晰，嘴微张，以线条表示额脊鬃毛，造型简洁，这三匹青铜马比“马踏飞燕”还要早400年左右',
                '该器物由三部分组成：酒樽盖、酒樽和托盘。顶端的酒樽盖隆起，重达1705克，上面的三只朱雀展翅欲飞。虽然中间的提环已残缺，但盖面上描绘的两周流云纹清晰可见。中间的酒樽为直桶状，腹部两侧透雕了蟠龙铺首衔环。侧壁外侧是两圈图案带，主要采用了细线镂刻手法和鎏金错银的工艺嵌入各种祥瑞图案形象，描绘有流云、鸟兽、奔鹿、羽人、西王母、侍者、山丘、奇花异草等神仙境界的生动画面。酒樽底部的三足成熊形，熊以肩乘盘，张口吐舌，形貌狰狞，通体镶嵌松绿石和衬以米色的水晶珠，与鎏金的器体相辉映。底部的托盘为宽平沿，浅直壁，三熊形足，比酒樽的熊形足稍小。托盘底部还阴刻纪年的48个隶书铭文。',
                '“酒海”是古时候人们对容量很大酒器称呼。此为邯郸市博物馆馆藏最大的盛酒器物——酒海。它的颈部有一圈文字：隆庆五年（公元1571年）二月韩氏吉造酒海。酒海周身修饰有褐彩花草纹饰，腹部还有八列文字：“贤良是孟江，孝顺是王祥。在家敬父母，何须远烧香。女贤是孟江，二郎担山赶太阳。三人哭活紫荆树，王祥卧冰救亲娘。”都是古代民间广泛流传的故事。',
                '此器物除了周身花草纹外，再无其他装饰，唯其肩部有一圈饶有意思的打油诗：“康熙八年，造下此坛。出在山西，郡名凌川，附城镇上，西南子山。”这句话交代了此物的制作地点。缸上还有一些广告词似的诗句：“放酒酒好，成醋醋酸，放水不漏，淹菜菜咸，诸般都放，放蜜更甜。”“买上一个，君常喜欢，人人爱买，不论价钱，使了想使，胜活十年。”而且，缸上有还许多口头趣言：“我要讨价，细细五钱”（意思是这个器物只卖五文钱）。“可好可好，直钱直钱。休走休走，快还快还，真正白货，去而何南。”意即这样的价钱买这个货物，简直就是白给您的了。走是太容易了，但是过了这村，就再也没有这个店了。把市井之间买家与卖家讨价还价的场面描绘得淋漓尽致，字里行间透露出淳朴的民窑气息和民俗文化特色。']
        for i in range(4):
            item=collection75Item()
            item["museumID"]=20
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item


        












