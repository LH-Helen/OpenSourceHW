import pymysql
class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(host='localhost',user='root',password='123456',database='beike_loupan',charset="utf8mb4")
            self.cursor = self.conn.cursor()  # 用来获得python执行Mysql命令的方法（游标操作）
            print("连接数据库成功")
        except:
            print("连接失败")

    def getItems(self):
        #获取数据表的内容
        sql= 'SELECT district,COUNT(id) FROM beijing_loupan GROUP BY district'    
        self.cursor.execute(sql)
        items = self.cursor.fetchall()  #接收全部的返回结果行
        return items