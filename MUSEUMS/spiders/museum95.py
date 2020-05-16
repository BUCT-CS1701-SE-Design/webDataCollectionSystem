import scrapy

from MUSEUMS.items import MuseumsItem
class Museum95Spider(scrapy.Spider):
    name = 'museum95'
    allowed_domains = ['gzchenjiaci.com']
    start_urls = ['http://www.gzchenjiaci.com/MYwebsite/rc/my_index.htm'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=95
        item['museumName'] = '广东民间工艺博物馆'
        item['introduction']='广东民间工艺博物馆以陈家祠为馆址，成立于1959年，国家一级博物馆。馆址陈家祠（匾额题陈氏书院）落成于清光绪十九年（1893年），是清代广东各地陈姓宗族在广州合资建造的合族祠，1988年被国务院公布为全国重点文物保护单位。陈家祠集岭南地区多种建筑装饰工艺于一体，包括有木雕、砖雕、石雕、陶塑、灰塑、铜铁铸和彩绘，被誉为“岭南建筑艺术的明珠”，是我国现存规模最大、保存最完好、装饰最精美的祠堂式建筑。'
        opentime=response.xpath("//*[@id='gnzx']/div/div[2]/p/text()").getall()
        item['opentime']=str(opentime[1])+str(opentime[2])+str(opentime[3])
        item['Link']='http://www.gzchenjiaci.com/'
        item['Location']=str(opentime[4])
        item['telephone']='020-81814559'
        yield item