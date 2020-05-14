import scrapy

from MUSEUMS.items import MuseumsItem
class Museum81Spider(scrapy.Spider):
    name = 'museum81'
    allowed_domains = ['hbww.org']
    start_urls = ['http://www.hbww.org/'] 
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.MuseumsPipeline': 1,}}
     
    def parse(self,response):
        item = MuseumsItem()
        item['museumID']=81
        item['museumName'] = '湖北省博物馆'
        item['Location']='湖北省武汉市武昌区东湖路160号'
        # response.xpath("//p[@class='appadd']/text()[1]").get().strip()
        item['Link']='http://www.hbww.org/'
        item['telephone']='027-86794127 / 027-86790329'
        # telephone=response.xpath("//p[@class='appadd']/text()[2]").get()
        item['introduction']='湖北省博物馆筹建于1953年，是全省最重要的文物征集与收藏、陈列展览与宣传教育机构，考古勘探、发掘和文物保护研究中心，是国家一级博物馆、中央和地方共建的八家国家级重点博物馆之一，国家文物局挂牌的饱水漆木器保护基地，中国博物馆协会乐器专委会主任委员单位，也是国家旅游局命名的“AAAAA”级旅游景区。湖北省博物馆位于风景秀丽的东湖之滨，占地面积123亩，现有建筑面积5万余平方米。主体建筑呈一主两翼“品”字形格局。整个建筑群高度体现了高台建筑、多层宽屋檐、大坡式屋顶等楚式建筑特点。湖北省文物考古研究所于1989年自湖北省博物馆分离，成为隶属于湖北省文化厅的独立法人单位，具备国家文物局认可的考古发掘团体领队资格，在湖北省文化厅（文物局）的领导下，主要担负湖北省境内的文物保护、考古发掘等项工作，承担配合大、中型基本建设的文物保护与考古调查、勘探、发掘任务，组织编写考古报告，开展科学研究。2002年湖北省博物馆与湖北省文物考古研究所合并。'
        item['opentime']='周二至周日 09:00—17:00（16:00后停止入馆），周一（法定节假日除外）、除夕当日闭馆'

    #     url='http://www.hbww.org/'+response.xpath("//div[@class='bottom_c']//ul[1]/li[1]/a[2]/@href").extract_first()
    #     yield scrapy.Request( url,callback=self.parse_detail,meta={"item":item})  
    # def parse_detail(self,response):
    #     item=response.meta["item"]
    #     # response.xpath("/html/body/div[6]/div[2]/div/div/text()").get().strip()
    #     introduction=response.xpath("//div[@class='inner']/div[2]/p/text()").getall()
    #     introduction="".join(introduction).strip()
        yield item