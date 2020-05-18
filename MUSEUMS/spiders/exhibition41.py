# -*- coding: utf-8 -*-
import scrapy
import copy
from MUSEUMS.items import exhibition75Item  # 声明使用的是那个Item

class Exhibition41Spider(scrapy.Spider):
    name = 'exhibition41'
    allowed_domains = ['zgyd1921.com']
    start_urls = [
        'http://www.zgyd1921.com/zgyd/node3/n11/n13/index.html']
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':1}
    }

    def parse(self, response):
        li_list = response.xpath("//ul[@class='piclist3']/li")
        for li in li_list:
            item = exhibition75Item()
            item["museumID"] = 41
            item["exhibitionTheme"] = li.xpath(".//p[@class='name']/a/text()").extract_first().strip()
            item["exhibition_picture"] = 'http://www.zgyd1921.com' + li.xpath("./a/img/@src").extract_first().strip()
            url = 'http://www.zgyd1921.com' + li.xpath("./a/@href").extract_first().strip()

            if('n52' in url):
                item["exhibitionIntroduction"] = '自1840年鸦片战争以来，中国开始遭受西方列强的大肆侵略和掠夺，逐步演变为半殖民地半封建社会。为了挽救国家和民族的危亡，中国人民进行了英勇的抗争和艰苦的探索，太平天国运动、洋务运动、维新变法运动、义和团运动、辛亥革命，这些探索和斗争虽然在一定程度上推动了中国社会的进步，但都未能改变中国的社会性质和人民的悲惨命运。挽救中国危亡的重任历史地落到新兴的无产阶级身上。'
            elif('n53' in url):
                item["exhibitionIntroduction"] = '1915年兴起的新文化运动，掀起了思想解放的浪潮。在俄国十月革命的影响下，陈独秀、李大钊等一批先进知识分子，经过五四运动的洗礼，从纷然杂陈的各种观点和学说中毅然选择了马克思主义。在共产国际的关注和推动下，上海、北京等地相继组建共产党早期组织，开展革命活动，大力宣传并促进马克思主义同中国工人运动相结合，为中国共产党的成立奠定了基础。'
            elif('n54' in url):
                item["exhibitionIntroduction"] = '1921年7月23日，中国共产党第一次全国代表大会在上海开幕。来自7个共产党早期组织的13位代表与2位共产国际代表出席会议。中国共产党第一次全国代表大会通过了党的纲领和工作决议，选举了中央领导机关，宣告中国共产党的正式成立。从此，中国出现了全新的、以马克思列宁主义为行动指南的，以实现社会主义和共产主义为奋斗目标的集中统一的无产阶级政党。中国革命的面目从此焕然一新。'
            yield item
