# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import exhibition75Item #声明使用的是那个Item
#声明使用的是那个Pipiline

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Exhibition75Pipeline': 5,}
    }
    name = 'exhibition26'
    allowed_domains = ['www.lnmuseum.com']
    start_urls = ['http://www.lnmuseum.com.cn/news/?ChannelID=650']
    def parse(self, response):
        names=['第一展厅 史前时期（距今约28万年——约4000年）',
               '第二展厅 夏商周时期（距今约4000年——约2500年）',
               '第三展厅  战国至隋唐时期（公元前五世纪——公元907年）',
               '第四展厅 辽金时期',
               '第五展厅  元明清时期（公元1234年——1840年）']
        imgs=['http://www.lnmuseum.com.cn/UpLoadFile/image/20170920/20170920143030603060.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20170920/20170920113447054705.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20170920/20170920113449834983.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20170920/20170920113391139113.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20170920/20170920113246084608.jpg']
        intros=['考古学一般将人类起源至农业出现以前的这一漫长时期称作“旧石器时代”， 这个时代以打制石器作为标志之一。辽宁是远古人类活动较早的地区之一，包括了旧石器时代早、中、晚期较完整的序列，其文化特征与华北的旧石器文化相近。其中金牛山人和小孤山人创造的物质文化水平，均居于人类进化史的前列，成为辽河文明的先导。',
                '距今约四千年以后，经过古国时代各地部族的文化交流、碰撞与融合，进入夏商王朝与周围方国并存时代。辽宁地区既有“与夏为伍”的夏家店下层文化，又有多类型的其他青铜文化，构成商周北土的不同部族方国。这些文化各具特色，又与中原夏商王朝保持着密切联系，是后来东北不同系统民族文化的源头。',
                '战国晚期中华大地呈现出从分裂逐步走向统一的态势。随着燕国势力的东进，东北南部纳入燕的版图，辽宁地区逐渐成为中原文化的一部分。秦汉时期，随着国家的繁荣强盛，中央王朝加快了开发东北的步伐，辽宁境内发现的这一时期的遗迹遗物，证明辽宁已经成为当时东北地区政治、经济、文的化中心，和向周边地区传播中原先进文化的枢纽。',
                '契丹族属东胡鲜卑族系，世居潢水（今西拉木伦河）和土河（今老哈河）流域，公元4世纪始见于史书记载，到唐末先后经历古八部、大贺氏和遥辇氏联盟三个时期。公元916年，迭剌部夷离堇兼联盟军事首领阿保机建立契丹（后改辽、大契丹、大辽）政权。辽朝极盛时期，疆域南据燕云，北至外兴安岭，东临日本海，西近阿尔泰山，是继匈奴、鲜卑、突厥、回鹘之后在北方兴起的又一个对中原产生巨大影响的游牧政权。历史上，辽宁地区是辽王朝版图的重要组成部分，考古发现的大量辽代遗迹遗物，反映了契丹族曾经的辉煌和辽文化的独特魅力。',
                '元朝是中国历史上第一个由少数民族蒙古族为主体建立的大一统帝国。蒙古族以其特有的进取精神推进了中国历史疆域形成与中华民族族体镕铸的新进程。辽宁地区虽饱受战争的创伤，但在元政府劝农政策的推动下，通过辽阳行省的管辖，以及各族人民的共同努力，农耕、商贸及手工业等经济逐渐恢复和发展。疆域的扩大和驿站的开辟，加速了民族的融合与交流，使得辽宁地区的文化展现出独特风采。']
        for i in range(5):  
            item=exhibition75Item()
            item["museumID"]=26
            item["exhibitionTheme"]=names[i]
            item["exhibition_picture"]=imgs[i]
            item["exhibitionIntroduction"]=intros[i]
            yield item  







