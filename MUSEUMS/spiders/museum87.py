import scrapy

from MUSEUMS.items import MuseumsItem
class Museum87Spider(scrapy.Spider):
    name = 'museum87'
    allowed_domains = ['ssmzd.com']
    start_urls = ['http://www.ssmzd.com/sitehtml/jlg/zlzd/gqzlt.htm'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=87
        item['museumName'] = '韶山毛泽东故居纪念馆'
        item['Link']='http://www.ssmzd.com/'
        item['Location']='湖南省湘潭市韶山区韶山冲'
        item['opentime']=response.xpath("//div[@style='padding:10px']/text()[6]").get().strip()+response.xpath("//div[@style='padding:10px']/text()[7]").get().strip()+response.xpath("//div[@style='padding:10px']/text()[8]").get().strip()
        item['telephone']='0731-55685157'
        url='http://www.ssmzd.com/sitehtml/jlg/bggk/bgjj.htm'
        yield scrapy.Request(url,callback=self.Others,meta={"item":item})
    def Others(self,response):
        item=response.meta["item"]
        introduction=response.xpath("//table[@width='90%']//text()").getall()
        item['introduction']="".join(introduction).strip() 
        yield item
