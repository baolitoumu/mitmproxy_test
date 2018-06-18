# -*- coding: utf-8 -*-

# Define your item pipelines here  
#  
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from twisted.enterprise import adbapi
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
import MySQLdb.cursors
import codecs
import json
from logging import log



class MySQLPipeline(object):
    def __init__(self,dbpool):
        self.dbpool=dbpool
        ''' 这里注释中采用写死在代码中的方式连接线程池，可以从settings配置文件中读取，更加灵活
            self.dbpool=adbapi.ConnectionPool('MySQLdb',
                                          host='127.0.0.1',
                                          db='crawlpicturesdb',
                                          user='root',
                                          passwd='123456',
                                          cursorclass=MySQLdb.cursors.DictCursor,
                                          charset='utf8',
                                          use_unicode=False)'''        
        
    
    @classmethod
    def from_settings(cls,settings):
        '''1、@classmethod声明一个类方法，而对于平常我们见到的则叫做实例方法。 
           2、类方法的第一个参数cls（class的缩写，指这个类本身），而实例方法的第一个参数是self，表示该类的一个实例
           3、可以通过类来调用，就像C.f()，相当于java中的静态方法'''
        dbparams=dict(
            host=settings['MYSQL_HOST'],#读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',#编码要加上，否则可能出现中文乱码问题
            cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=False,
        )
        
        dbpool=adbapi.ConnectionPool('MySQLdb',**dbparams)#**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        return cls(dbpool)#相当于dbpool付给了这个类，self中可以得到

    #pipeline默认调用
    def process_item(self, item, spider):
        query=self.dbpool.runInteraction(self._conditional_insert,item)#调用插入的方法
        query.addErrback(self._handle_error,item,spider)#调用异常处理方法
        return item
    
    #写入数据库中
    def _conditional_insert(self,tx,item):
        #print item['name']
        sql="insert into testtable(numFound,currPage,totalPage,ershouCount,idleCount,ershou,user_Icon,user_Nick,user_vipLevel,user_TypeId,user_isTaobaoWomen,user_taobaoWomenUrl,user_CreditUrl,user_ItemsUrl,user_isSinaV,user_yellowSeller,item_imageUrl,item_imageHeight,item_imageWidth,item_Url,item_isBrandNew,item_price,item_orgPrice,item_provcity,item_describe,item_publishTime,item_From,item_FromDesc,item_FromTarget,item_commentCount,item_commentUrl,item_collectCount,item_title) values(%s,%s)"
        
        
    
        params = (
            item['numFound'],
            item['currPage'],
            item['totalPage'] ,
            item['ershouCount'],
            item['idleCount'] ,
            item['ershou'] ,
    
            item['user_Icon'],
            item['user_Nick'],
            item['user_vipLevel'] ,
            item['user_TypeId'] ,
            item['user_isTaobaoWomen'] ,
            item['user_taobaoWomenUrl'] ,
            item['user_CreditUrl'] ,
            item['user_ItemsUrl'],
            item['user_isSinaV'] ,
            item['user_yellowSeller'] ,
            
            item['item_imageUrl'] ,
            item['item_imageHeight'],
            item['item_imageWidth'] ,
            item['item_Url'] ,
            item['item_isBrandNew'] ,
            item['item_price'] ,
            item['item_orgPrice'] ,
            item['item_provcity'],
            item['item_describe'] ,
            item['item_publishTime'] ,
            item['item_From'] ,
            item['item_FromDesc'] ,
            item['item_FromTarget'] ,
            item['item_commentCount'] ,
            item['item_commentUrl'] ,
            item['item_collectCount'] ,
            item['item_title'],
        )
        tx.execute(sql,params)
    
    
    #错误处理方法
    def _handle_error(self, failue, item, spider):
        print ('--------------database operation exception!!-----------------')
        print ('-------------------------------------------------------------')
        print (failue)

