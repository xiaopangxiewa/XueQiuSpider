# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class XueqiuPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host='127.0.0.1',user='root',passwd='root',
                                  db='xueqiu',charset='utf8')
        
    def process_item(self, item, spider):
        cur=self.conn.cursor()
        for i in range(len(item['title'])):
            title=item['title'][i]
            ndetail=item['detail'][i]
            sql='insert into stocknews(wtitle,wdetail) values(%s,%s)'
            try:
                cur.execute(sql,(title,ndetail))
            except Exception as err:
                print(err)
    def close_spider(self):
        self.conn.close()
            
