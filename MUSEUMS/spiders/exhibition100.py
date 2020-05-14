import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition100Spider(scrapy.Spider):
    name = 'exhibition100'
    allowed_domains = ['sxd.cn']
    start_urls = ['http://www.sxd.cn/showinfo.asp?id=9&bigclass=23','http://www.sxd.cn/showinfo.asp?id=10&bigclass=23'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=100
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//td[@valign='top']//tr[2]//tr/td/text()").get().strip()
        ex=response.xpath("//td[@valign='top']//tr[2]//tr[2]//text()").getall()
        item['exhibitionIntroduction']="".join(ex).strip().split('分享到',1)[0].strip()
        item['exhibition_picture']='http://www.sxd.cn/'+response.xpath("//td[@valign='top']//tr[2]//tr[2]//p[@align='center']//@src").get()
        yield item