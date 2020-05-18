import scrapy
from MUSEUMS.items import collection75Item

class Exhibition75Spider(scrapy.Spider):
    custom_settings={
        'ITEM_PIPELINES':{'MUSEUMS.pipelines.Collection75Pipeline':4,}
    }
    name = 'collection26'
    allowed_domains = ['www.lnmuseum.com']
    start_urls = ['http://www.balujun.cn/']
    def parse(self, response):
        names=['燕王职戈',
               '迦陵频伽纹镜',
               '耀州窑青瓷飞鱼形水盂',
               '彩釉塑贴云龙纹三足罐',
               '铜鎏金大威德金刚',
               '木雕罗汉像',
               '王蒙太白山图',
               '']
        imgs=['http://www.lnmuseum.com.cn/UpLoadFile/image/20141104/2014110414290218218.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20141104/20141104142437723772.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/maxpic201312/20131217111656.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20141013/20141013130286468646.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20141104/20141104112386758675.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/maxpic201312/20131217142103.jpg',
              'http://www.lnmuseum.com.cn/UpLoadFile/image/20141105/20141105104212461246.jpg']
        intros=['形体大，中部有隆起的脊，脊旁有凹形血槽，胡作三弧线，阑内三穿，直内一穿，内铸虎纹，胡上铸铭文：“郾王职乍御司马”。为燕王作，为其御司寇所用之兵器。器精美而文字史料价值极高。',
                '镜子呈圆形，镜心有破孔，背面铸突起的迦陵频伽纹，主纹空隙填涂黑漆，使花纹生动突出。迦陵频伽为梵语，译为美妙声音，汉译多做“妙音鸟”常见于佛教雕刻，一般作人首鸟身形象。佛经说迦陵是仙鸟，在卵壳中，鸣音已压众鸟，所以说佛法之音与之相似。辽代用此图纹作镜，可见契丹人深信佛教的程度。',
                '整体造型设计成龙鱼形，上颚向上翻卷，双翅高振呈飞翔状，鱼尾商桥，呈“U”字形，器内隔成前后两室，底置小圈足。白瓷胎，胎质细腻坚硬。内外施满青釉，釉色润泽晶莹、青翠欲滴，足根无釉。',
                '高领外侈、敞口，球形腹，下承三兽形足，有窑沾。腹部中央装饰一周凸弦纹，淋釉，器底部无釉露胎，胎质细腻。上腹部贴塑三个动物纹饰，腹部正中贴塑舞狮。器型饱满，线条柔和。',
                '此尊为九头三十四臂，九头分三层排列，正面为牛头，牛角粗大，血盆大口，头戴五骷髅冠；最上一头，为如来相，象征着他是阿弥陀佛化身而来。最下面七头，头顶红发上竖，象征忿怒。上身饰璎珞，下身围虎皮，顶挂五十人头骨串。主二臂抱明妃，其余手伸向两边，诸手皆持法器，铃、杵、刀、剑、弓、箭、瓶、索子、钩、戟、伞、盖、骷髅等兵器，各有寓意。有十六条腿，皆左展姿站立，左右脚分别踩八种人、兽和禽。明妃罗浪杂娃坐在主尊怀中，右手持月刀，左手持人心，左腿勾在主尊腰间，右脚踩飞禽。下为单层覆莲座。此尊形象复杂，面目手足众多，但布局简洁明了，线条一丝不苟。台座上刻“大清乾隆御制”楷书款。',
                '此尊呈比丘相，圆睁双目，面相威严，棱角分明。内穿交领僧衣，外穿通肩式袈裟，以丝带束于腰间。衣纹厚重流畅，裙下摆自然搭于台座上。左手结法印，右手置腿上抓大衣一角，极其出色地突出了布料的质感。结跏趺坐姿。台座为岩石状高台座。罗汉是佛教造像的主要题材之一，形象仿照现实生活中的僧人特点，以印度僧人形象为多。光头，无肉髻，身披袈裟或大领僧衣。相貌不一，手法或夸张或写实，神韵生动。',
                '绘浙江鄞县太白山天童寺及其周围景物，尤其着重描绘天童寺前二十里夹径松林。画面中远岫层峦，溪流潺潺，人物往还其间，用笔松润，赋色淡雅。画心右上角有小字篆书“太白山图”四字，画尾钤“王蒙印”，近人研究认为此卷为王蒙晚年代表作。']
        for i in range(7):  
            item=collection75Item()
            item["museumID"]=26
            item['collectionName']=names[i]
            item['collectionImage']=imgs[i]
            item['collectionIntroduction']=intros[i]
            yield item  








