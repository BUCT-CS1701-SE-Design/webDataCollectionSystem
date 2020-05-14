# -*- coding: utf-8 -*-
import scrapy
from MUSEUMS.items import collection75Item
#声明使用的是那个Pipiline
custom_settings={
      'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
class Collection75Spider(scrapy.Spider):
    name = 'collection4'
    allowed_domains = ['jb.mil.cn']
    start_urls = ['http://www.jb.mil.cn/was/web/search?token=14.1499419140318.94&channelid=237727']
    
    def parse(self, response):
        li_list=response.xpath("//div[@class='relicAppRight']/div[@class='raAppList']/ul/li")
        for li in li_list:
            item=collection75Item()
            item["museumID"]=4
            url=li.xpath("./a/@href").extract_first()
            yield scrapy.Request(
                        url,
                        callback=self.parse_detail,
                        meta={"item":item}#传递参数
        )
    def parse_detail(self,response):
        item=response.meta["item"]
        item['collectionName']=response.xpath("//div[@class='interContext']/h2/text()").extract_first()
        item['collectionImage']='http://www.jb.mil.cn/gcww/wwjs_new/shzysq/201707/'+response.xpath("//img[@border='0']/@oldsrc").extract_first()
        
        #从这以上的代码都是没问题的 都是写好的 Name 和 Image都是爬完的
        #就是下面这个Introduction还没有爬取成功
        #http://www.jb.mil.cn/gcww/wwjs_new/shzysq/201707/t20170705_32875.html  这是关于彭桓武的那个url

        #这两行代码是我测试<p>能不能被找到
        data=response.xpath("//div[@class='interaction']/div[@class='interContext']/p")
        item['collectionIntroduction']="这个有点难爬,后面再改"
        yield item

        



