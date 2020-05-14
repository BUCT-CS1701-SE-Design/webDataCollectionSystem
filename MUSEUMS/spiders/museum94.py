import scrapy

from MUSEUMS.items import MuseumsItem
class Museum94Spider(scrapy.Spider):
    name = 'museum94'
    allowed_domains = ['guangzhoumuseum.cn']
    start_urls = ['http://www.guangzhoumuseum.cn/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=94
        item['museumName'] = '广州博物馆'
        item['introduction']='广州博物馆位于广州风景秀丽的越秀山，馆址镇海楼。镇海楼建于明洪武十三年（1380年），是永嘉侯朱亮祖修缮广州城时，北城垣拓展至越秀山上时建造的城楼。镇海楼自清代以来，多次被评为羊城八景和现代十大旅游美景之一。1928年，广州市政府在修葺的同时，于此筹办“广州市立博物院”，1929年2月11日，正式对外开放，为我国最早期创建的博物馆之一。1941—1945年，称为广州市立图书博物馆。1946—1949年，称为广州市立博物馆。1950年至现在，称为广州博物馆。广州博物馆经过不断发展，现除镇海楼展区外，同时还有广州美术馆、三元里人民抗英斗争纪念馆、三·二九起义指挥部旧址纪念馆三个分展区 广州博物馆是一座具有地方特色的综合性历史博物馆，是收藏和展示广州地方历史文物的重要场所。现馆内常设展览为“广州历史陈列”展，展览通过近千件古、近代的图片、资料，使人们从中了解到广州历史发展的概况与地方文化的特征。此外，广州博物馆还定期举办各类专题性、纪念性的临展。'
        item['opentime']='周一闭馆，周二至周四9:00—17:30（17时停止售票、进场），周五至周日9:00-21:00（20:30停止售票、进场）。如遇国家法定节假日正常开放。'
        item['Link']='http://www.guangzhoumuseum.cn/'
        item['Location']='广州市越秀公园内镇海楼'
        item['telephone']='020-83550627'
        yield item