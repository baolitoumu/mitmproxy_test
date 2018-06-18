
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
from scrapy.utils.project import get_project_settings #导入seetings配置

class DBHelper():
    
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''
    def __init__(self):
        self.settings=get_project_settings() #获取settings配置，设置需要的信息
        
        
        self.host=self.settings['MYSQL_HOST']
        self.port=self.settings['MYSQL_PORT']
        self.user=self.settings['MYSQL_USER']
        self.passwd=self.settings['MYSQL_PASSWD']
        self.db=self.settings['MYSQL_DBNAME']
    
    #连接到mysql，不是连接到具体的数据库
    def connectMysql(self):
        host=  self.host
        print('host++++++++',host)
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             #db=self.db,不指定数据库名
                             charset='utf8') #要指定编码，否则中文可能乱码
        return conn
    #连接到具体的数据库（settings中设置的MYSQL_DBNAME）
    def connectDatabase(self):
        conn=MySQLdb.connect(host=self.host,
                             port=self.port,
                             user=self.user,
                             passwd=self.passwd,
                             db=self.db,
                             charset='utf8') #要指定编码，否则中文可能乱码
        return conn   
    
    #创建数据库
    def createDatabase(self):
        '''因为创建数据库直接修改settings中的配置MYSQL_DBNAME即可，所以就不要传sql语句了'''
        conn=self.connectMysql()#连接数据库
        
        sql="create database if not exists "+self.db
        cur=conn.cursor()
        cur.execute(sql)#执行sql语句
        cur.close()
        conn.close()
    
    #创建表
    def createTable(self,sql):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.close()
    #插入数据
    def insert(self,sql,*params):#注意这里params要加*,因为传递过来的是元组，*表示参数个数不定
        conn=self.connectDatabase()
        
        cur=conn.cursor();
        cur.execute(sql,params)
        conn.commit()#注意要commit
        cur.close()
        conn.close()
    #更新数据
    def update(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()#注意要commit
        cur.close()
        conn.close()
    
    #删除数据
    def delete(self,sql,*params):
        conn=self.connectDatabase()
        
        cur=conn.cursor()
        cur.execute(sql,params)
        conn.commit()
        cur.close()
        conn.close()
        
        

'''测试DBHelper的类'''
class TestDBHelper():
    def __init__(self):
        self.dbHelper=DBHelper()
               
    #测试创建数据库（settings配置文件中的MYSQL_DBNAME,直接修改settings配置文件即可）
    def testCreateDatebase(self):
        self.dbHelper.createDatabase() 
    #测试创建表
    def testCreateTable(self):
        sql="create table sony(id int primary key auto_increment,city_code int(10),city_name varchar(200), city_name_province varchar(200), city_url varchar(200), currPage int(10), district varchar(200), district_url varchar(200),ershou int(10),ershouCount int(10),final_url varchar(200),firstlevel_title varchar(200),firstlevel_url varchar(200),idleCount varchar(200),item_From varchar(200),item_FromDesc varchar(200),item_FromTarget varchar(200),item_Url varchar(200),item_collectCount varchar(200),item_commentCount varchar(200),item_commentUrl varchar(200),item_describe varchar(200),item_imageHeight varchar(200),item_imageUrl varchar(200),item_imageWidth varchar(200),item_isBrandNew varchar(200),item_orgPrice varchar(200),item_price varchar(200),item_provcity varchar(200),item_publishTime varchar(200),item_title varchar(200),numFound varchar(200),threelevel varchar(200),threelevel_url varchar(200),totalPage varchar(200),twolevel varchar(200),twolevel_url varchar(200),user_CreditUrl varchar(200),user_Icon varchar(200),user_ItemsUrl varchar(200),user_Nick varchar(200),user_TypeId int(3),user_isSinaV int(3),user_isTaobaoWomen int(3),user_taobaoWomenUrl varchar(200),user_vipLevel varchar(200),user_yellowSeller varchar(200),word varchar(200))"

        
        self.dbHelper.createTable(sql)
    #测试插入
    def testInsert(self):
        sql="insert into sony(name,url) values(%s,%s)"
        params=("test","test")
        self.dbHelper.insert(sql,*params) #  *表示拆分元组，调用insert（*params）会重组成元组
    def testUpdate(self):
        sql="update sony set name=%s,url=%s where id=%s"
        params=("update","update","sony")
        self.dbHelper.update(sql,*params)
    
    def testDelete(self):
        sql="delete from sony where id=%s"
        params=("sony")
        self.dbHelper.delete(sql,*params)
    
if __name__=="__main__":
    testDBHelper=TestDBHelper()
    #testDBHelper.testCreateDatebase()  #执行测试创建数据库
    testDBHelper.testCreateTable()     #执行测试创建表
    #testDBHelper.testInsert()          #执行测试插入数据
    #testDBHelper.testUpdate()          #执行测试更新数据
    #testDBHelper.testDelete()          #执行测试删除数据
