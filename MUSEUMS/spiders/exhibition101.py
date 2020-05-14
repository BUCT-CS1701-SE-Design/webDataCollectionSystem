import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition101Spider(scrapy.Spider):
    name = 'exhibition101'
    allowed_domains = ['wuhouci.net.cn']
    start_urls = ['http://www.wuhouci.net.cn/visit-top.html'] 
    def parse(self, response):
        pass