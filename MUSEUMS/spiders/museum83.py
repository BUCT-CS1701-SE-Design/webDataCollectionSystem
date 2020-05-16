import scrapy

from MUSEUMS.items import MuseumsItem
class Museum83Spider(scrapy.Spider):
    name = 'museum83'
    allowed_domains = ['whmuseum.com.cn']
    start_urls = ['http://www.whmuseum.com.cn/survey'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=83
        item['museumName'] ='武汉博物馆'
        opentime=response.xpath("//div[@class='openinfo']/div/h3/text()").getall()
        item['opentime']="".join(opentime).strip()
        item['Link']='http://www.whmuseum.com.cn/'
        item['Location']='武汉市江汉区青年路373号'
        # item['Location']=response.xpath("//footer//ul[@class='ewmbox']/li[1]/p/font/font/text()").get()
        # item['telephone']=response.xpath("//footer//ul[@class='ewmbox']/li[2]/p/text()").get()
        item['telephone']='027-85601720'
        # introduction=response.xpath("//p[@class='cont']/text()").getall()
        # item['introduction']="".join(introduction).strip()
        item['introduction']='武汉博物馆是武汉市重要的文化窗口和艺术殿堂，展示着这座华中都会源远流长的发展轨迹和博大精深的文化积淀，承载着历代武汉人民的历史文脉与煌煌业绩，播扬着当代武汉现在的武汉博物馆已经发展为集文物收藏、学术科研、社会教育、文化交流、休闲娱乐等功能于一体的现代化综合性博物馆。'
        yield item