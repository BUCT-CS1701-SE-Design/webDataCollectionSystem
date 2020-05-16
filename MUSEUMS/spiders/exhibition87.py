import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition87Spider(scrapy.Spider):
    name = 'exhibition87'
    allowed_domains = ['ssmzd.com']
    start_urls = ['http://www.ssmzd.com/jngclzl/jngcl/Index.html'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=87
        url1=[]
        url1+=response.xpath("/html/body/table[2]/tr/td/table/tr[2]/td[1]/table[2]/tr[3]/td/a/@href").getall()
        url1+=response.xpath("/html/body/table[2]/tr/td/table/tr[2]/td[1]/table[2]/tr[5]/td/a/@href").getall()
        for url in url1:
            url='http://www.ssmzd.com'+url
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        some=response.xpath("/html/body/table[2]/tr/td/table/tr[2]/td[2]/table/tr[2]/td/table")
        a=-1
        for temp in some:
            a+=1
            if a==0:
                continue
            item=response.meta["item"]
            # exhibitionTime=
            item['exhibitionTheme']=temp.xpath("./tr/td[1]/table/tr/td/a/@title").get()
            item['exhibitionIntroduction']=temp.xpath("./tr/td[2]/table[2]/tr/td/text()").get()
            pic=temp.xpath("./tr/td[1]/table/tr/td/a/img/@src").getall()
            d="".join(pic).strip()
            if d=='':
                item['exhibition_picture']=''
            else:
                item['exhibition_picture']='http://www.eywsqsfbwg.com/'+d
            if a>5:
                break
            yield item  