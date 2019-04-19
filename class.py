class Db():
    # 构造函数
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.host = '127.0.0.1'
        self.port = '3306'

    def conn(self):
        print(self.host, self.port, self.username, self.password)

db = Db('pigfly', '123')
db.host = '113.56.10.98';
db.conn()

db = Db('zhupp', '456')
db.conn()

# 继承
class MySQL(Db):
    def query(self, sql):
        print(sql)

mysql = MySQL('zz', '0123')
mysql.conn()
mysql.query('select * from users')