import scrapy
from MUSEUMS.items import exhibition75Item
class Exhibition92Spider(scrapy.Spider):
    name = 'exhibition92'
    allowed_domains = ['sunyat-sen.org']
    start_urls = ['http://www.sunyat-sen.org/index.php?m=content&c=index&a=lists&catid=53'] 
    custom_settings={
       'ITEM_PIPELINES':{'MUSEUMS.pipelines.ExhibitionPipeline':5,}}
    def parse(self, response):
        item=exhibition75Item()
        item["museumID"]=92
        url1=response.xpath("//div[@id='con_zzjs_1']/ul/li//@href").getall()
        for url in url1:
            url='http://www.sunyat-sen.org'+url
            yield scrapy.Request(url,callback=self.Intro,meta={"item":item})
    def Intro(self,response):
        item=response.meta["item"]
        # exhibitionTime=
        item['exhibitionTheme']=response.xpath("//p[@class='dh']/a[4]/text()").get()
        ex=response.xpath("//div[@class='ng_box']/div//text()").getall()
        item['exhibitionIntroduction']="".join(ex).strip().replace('\t','').replace('\r\n','')
        '''pic=response.xpath("//div[@class='ng_box']/div//@src").getall()
        a=0
        while a+1<=len(pic):
            pic[a]='http://www.eywsqsfbwg.com/'+pic[a]
            a+=1    
        item['exhibition_picture']="".join(pic)'''
        item['exhibition_picture']='http://www.eywsqsfbwg.com/'+response.xpath("//div[@class='ng_box']/div//@src").get()
        # yield item 
        print(item)