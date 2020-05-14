import scrapy

from MUSEUMS.items import MuseumsItem
class Museum97Spider(scrapy.Spider):
    name = 'museum97'
    allowed_domains = ['amgx.org']
    start_urls = ['http://www.amgx.org/news-2076.html'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=97
        item['museumName'] = '广西民族博物馆'
        opentime=response.xpath("//div[@class='mbdetial']//p[2]/text()[2]").get().strip().split("馆",1)
        item['opentime']=opentime[1]+':'+response.xpath("//div[@class='mbdetial']//p[2]/text()[3]").get().strip()
        item['Link']='https://www.amgx.org/'
        telephone=response.xpath("//div[@class='mbdetial']//p[2]/text()[16]").get().strip().split("：",1)
        item['telephone']=telephone[1]
        url= response.xpath("//td[@valign='top']/p/a[7]/@href").get()
        yield scrapy.Request(url,callback=self.IntroM,meta={"item":item})
    def IntroM(self,response):
        item=response.meta["item"]
        item['Location']='南宁市青秀山风景区青环路11号'
        introduction=response.xpath("//div[@class='listint']/div/p/text()").getall()
        item['introduction']="".join(introduction).strip()
        yield item
