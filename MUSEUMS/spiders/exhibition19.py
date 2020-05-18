# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition19'
    allowed_domains = ['www.hdmuseum.org']
    start_urls = ['http://www.xbpjng.cn/PlatNews/platform.aspx?c=8c812025-0ca3-4ffb-80b0-1912dfe73c39&z=3746daa2-306c-4092-816b-c3f793d32e28']
    def parse(self, response):
        names=['西柏坡纪念馆-第一展室',
               '西柏坡纪念馆-第二展室',
               '西柏坡纪念馆-第三展室',
               '西柏坡纪念馆-第四展室',
               '西柏坡纪念馆-第五展室']
        intros=['1947年初，国民党军队全面进攻解放区失败后，改为重点进攻陕北和山东解放区。3月18日，中共中央主动撤离延安。在枣林沟，中共中央决定：毛泽东、周恩来、任弼时等组成中央前委，继续留在陕北，指挥全国的解放战争；刘少奇、朱德等组成中央工委向华北转移，进行中央委托的工作。西柏坡位于河北省平山县中部。平山县具有光荣的革命传统、优越的战略位置、得天独厚的地理条件和良好的群众基础。同年5月，中央工委进驻建屏(今平山)县西柏坡。',
                '中央工委在西柏坡召开全国土地会议，领导解放区的土地改革运动和整党工作，冲击了几千年来的封建土地制度，提高了党组织的战斗力，为解放战争的胜利发展奠定了基础。',
                '在中央工委的指导下，晋察冀野战军先后取得了青沧战役、大清河北战役、保北战役、清风店战役、石家庄(石门)战役的胜利，扭转了晋察冀军事斗争的局面。特别是石家庄的解放，使晋察冀和晋冀鲁豫两大解放区联成一片，为中共中央移驻西柏坡创造了有利条件。',
                '根据中共中央指示，建立了华北财经办事处，逐步建立起财政管理的各项规章制度，使解放区经济有了较大的发展，为统一解放区的财经工作创造了有利条件。',
                '1948年春，全国战场形势发生了根本变化。为了更有力地领导和指挥全国的解放战争，中央前委毛泽东、周恩来、任弼时等东渡黄河，移驻西柏坡。在西柏坡召开的九月会议，为人民解放军与国民党军队进行战略决战，夺取新民主主义革命的胜利，从思想上、政治上和组织上做了重要准备。']
        for i in range(5):  
            item=exhibition75Item()
            item["museumID"]=19
            item["exhibitionTheme"]=names[i]
            item["exhibition_picture"]="无法获取"
            item["exhibitionIntroduction"]=intros[i]
            yield item  




