import scrapy

from MUSEUMS.items import MuseumsItem
class Museum85Spider(scrapy.Spider):
    name = 'museum85'
    allowed_domains = ['zhongshanwarship.org.cn']
    start_urls = ['http://www.zhongshanwarship.org.cn/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=85
        item['museumName'] ='武汉中山舰博物馆'
        item['opentime']=response.xpath("//div[@class='footer']//span/p/text()[1]").get().strip()
        item['Link']='http://www.zhongshanwarship.org.cn/'
        item['Location']=response.xpath("//div[@class='footer']//span/p/text()[2]").get().strip()
        item['telephone']=response.xpath("//div[@class='footer']//span/p/text()[3]").get().strip()
        introduction=response.xpath("//*[@id='bwgJianJie']/text()").getall()
        item['introduction']="".join(introduction).strip()
        yield item