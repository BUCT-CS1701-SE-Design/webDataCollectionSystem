import scrapy
import urllib.request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from MUSEUMS.items import MuseumsItem
class Museum80Spider(scrapy.Spider):
    name = 'museum80'
    allowed_domains = ['eywsqsfbwg.com']
    start_urls = ['http://www.eywsqsfbwg.com/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}   
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=80
        item['museumName']='鄂豫皖苏区首府革命博物馆'
        Location=response.xpath("//div[@class='ind_ykxz']/text()[4]").get().strip()
        item['Location']=Location=response.xpath("//div[@class='ind_ykxz']/text()[4]").get().strip()
        item['Link']='http://www.eywsqsfbwg.com/'
        item['telephone']='0376-2987315'
        item['opentime']=response.xpath("//div[@class='ind_ykxz']/text()[2]").get()+response.xpath("//div[@class='ind_ykxz']/text()[3]").get()
        url=response.xpath("/html/body/div[2]/div[1]/div/ul/li[2]/div/dl/dd[1]/a/@href").extract_first()
        yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//div[@class='inner']/div[2]/p/text()").getall()
        introduction="".join(introduction).strip()
        item['introduction']=introduction
        yield item
  
       
