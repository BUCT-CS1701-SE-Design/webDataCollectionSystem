# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

#博物馆
class MuseumsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    museumID=scrapy.Field()
    museumName = scrapy.Field()
    introduction=scrapy.Field()
    opentime=scrapy.Field()
    Link=scrapy.Field()
    Location=scrapy.Field()
    telephone=scrapy.Field()

'''class eucation75Item(scrapy.Item):
    museumID=scrapy.Field()
    eucationID=scrapy.Field()
    educationName=scrapy.Field()
    educationLink=scrapy.Field()
class academic75Item(scrapy.Item):
    museumID=scrapy.Field()
    academicResearchID=scrapy.Field()
    academicResearchTime=scrapy.Field()
    academicResearchTitle=scrapy.Field()
    academicResearchLink=scrapy.Field()'''
#藏品
class collection75Item(scrapy.Item):
    museumID=scrapy.Field()
    collectionID=scrapy.Field()
    collectionName=scrapy.Field()
    collectionIntroduction=scrapy.Field()
    collectionImage=scrapy.Field()#图片链接
    #collectionLink=scrapy.Field()#一般不用
#展览
class exhibition75Item(scrapy.Item):
    museumID=scrapy.Field()
    #exhibitionID=scrapy.Field()
    exhibitionTime=scrapy.Field()
    exhibitionTheme=scrapy.Field()
    exhibitionIntroduction=scrapy.Field()
    exhibition_picture=scrapy.Field()
    #exhibitionIntroductionLink=scrapy.Field()

