# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import os
import re
import pymysql
import logging
logger = logging.getLogger(__name__)
MYSQL_HOST = 'rm-bp1k0s6kbpm66bpfc4o.mysql.rds.aliyuncs.com'
MYSQL_DBNAME = 'museumapplication'
MYSQL_USER = 'test1'
MYSQL_PASSWD = 'test1'  
#博物馆表
class MuseumsPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        item["introduction"]=self.process_content(item["introduction"])
        insert_sql = "INSERT INTO museum(museumID, museumName,introduction,opentime,Link,location,telephone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (item['museumID'], item['museumName'], item['introduction'], item['opentime'], item['Link'], item['Location'], item['telephone'])
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()      
    #处理数据的函数，根据自己情况设置
    def process_content(self,introduction):
        content=''
        for i in introduction:
            content+=i
        introduction=content
        return introduction   
#藏品表
class Collection75Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        #print(item)
        insert_sql = "INSERT INTO collection(museumID,collectionName,collectionIntroduction,collectionImage) VALUES ('%s', '%s', '%s', '%s')" % (item['museumID'], item['collectionName'], item['collectionIntroduction'], item['collectionImage'])
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
#展览表
class Exhibition75Pipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=MYSQL_HOST,
            db=MYSQL_DBNAME,
            user=MYSQL_USER,
            passwd=MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        insert_sql = "INSERT INTO exhibition(museumID,exhibitionTheme,exhibition_picture) VALUES ('%s', '%s', '%s')" % (item['museumID'], item['exhibitionTheme'], item['exhibition_picture'])
        self.cursor.execute(insert_sql)

        # 4. 提交操作
        self.connect.commit()
        return item
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
    


