# -*- coding: UTF-8 -*-
from scrapy import cmdline
'''import pymysql
 
# 建立数据库连接
db=pymysql.connect(
    host='rm-bp1k0s6kbpm66bpfc4o.mysql.rds.aliyuncs.com',
    user='test1',
    password='test1',
    db='museumapplication',
    charset='utf8'
)
 
# 获取游标
cursor=db.cursor()
# 执行sql语句
# sql='delete from collection where where museumID>=1 and museumID<=130'
# rows=cursor.executemany(sql,[('2'),('3')]) 
sql="DELETE FROM collection WHERE museumID>=1 and museumID<=130"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
   
except:
   # 发生错误时回滚
   db.rollback()

sql="DELETE FROM exhibition WHERE museumID>=1 and museumID<=130"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()

except:
   # 发生错误时回滚
   db.rollback()
   

# 提交
# conn.commit()

# 关闭游标
# cursor.close()

# 关闭连接
db.close()'''

cmdline.execute("scrapy crawlall".split())