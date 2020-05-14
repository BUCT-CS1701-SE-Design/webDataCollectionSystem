# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline
custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
class Exhibition75Spider(scrapy.Spider):
    name = 'exhibition8'
    allowed_domains = ['www.bmnh.org.cn']
    start_urls = ['http://www.bmnh.org.cn/zljs/jbcl/1/zljs/index.shtml']
    def parse(self, response):
         list=response.xpath("//div[@class='perexh_items']")
         for div in list:
             item=exhibition75Item()
             item["museumID"]=8
             url='http://www.bmnh.org.cn'+div.xpath("./a/@href").extract_first()
             yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item["exhibitionTheme"]=response.xpath("//div[@class='content_singler']/p[@class='single_title']/text()").extract_first()
        item["exhibition_picture"]='http://www.bmnh.org.cn'+response.xpath("//div[@class='single_block']/p[@class='clp1']/img/@src").extract_first()     
        content=''
        list=response.xpath("//p[@style='text-indent: 2em;']/span/text()").extract()
        for i in list:
            content+=i
        item["exhibitionIntroduction"]=content
        if item["exhibitionTheme"]=='《古爬行动物》':
            item["exhibitionIntroduction"]="古爬行动物厅向观众展示了生物界两亿多年前的景观，并以总鳍鱼、鱼石螈、蚓螈和异齿龙为代表，演示了脊椎动物从水域向陆地发展的复杂过程。大厅中央展示了栩栩如生的恐龙骨架群，如中国人发现的第一条恐龙——许氏禄丰龙，体长达26米的井研马门溪龙，称王称霸的霸王龙，小巧玲珑的恐爪龙，背上布满剑板的沱江龙，威风凛凛的永川龙，展翅翱翔的翼龙，称霸海洋的鱼龙。多媒体电脑可以让观众欣赏到恐龙的原始埋藏状态，并通过“化石搜寻器”来体味古生物学家挖掘恐龙化石的艰辛和乐趣，从模拟地层演示中体会到地球沧海变良田式的重大地质变化过程......"
        if item["exhibitionTheme"]=='《无脊椎动物的繁荣》':
            item["exhibitionIntroduction"]="无脊椎动物的繁荣”展览重点讲述了化石的形成、生命的起源，寒武纪大爆发，无脊椎动物的繁荣等重大历史事件；清晰地展示了从原核生物到真核生物，从单细胞的原生动物到多细胞的后生动物，又历经二胚层阶段、三胚层阶段最后到脊椎动物起源的生命进化历程。"
        if item["exhibitionTheme"]=='《恐龙公园》':
            item["exhibitionIntroduction"]="""北京自然博物馆与观众阔别一年多的《恐龙公园》经过了脱胎换骨的改造之后，于2013年暑假又与观众见面了！改造后的《恐龙公园》焕然一新，23条活灵活现的恐龙、两只翼龙以及一只和最早恐龙生活在一起的坚喙蜥构成了不同的组合，分别代表了从三叠纪晚期到白垩纪晚期不同时期的恐龙世界的面貌。这次对《恐龙公园》的改造，主要是利用更加先进的技术手段，使复原的恐龙更加逼真。这些恐龙除了摇头摆尾、张牙舞爪、吼叫嘶鸣等传统动作之外，北京自然博物馆还特别增加了恐龙眨眼、喘气等细节动作，使恐龙更加栩栩如生。"""
        if item["exhibitionTheme"]=='《植物世界》':
            item["exhibitionIntroduction"]="《植物世界》是北京自然博物馆自1958年建馆以来一直保留的四大经典常设展陈之一。2018年它迎来了第四次更新改造，经过几个月的精心制作，6月29日正式对外开放。更新后的展览位于北京自然博物馆展览楼二楼北侧，展览面积850余平方米，展出的植物化石和各类现代植物标本多达1200余件，三个展厅分设 “植物演化”、“被子植物的繁盛与适应”和“植物与人类”三部分内容。"
        if item["exhibitionIntroduction"] !='':
         yield item
       
       

        





