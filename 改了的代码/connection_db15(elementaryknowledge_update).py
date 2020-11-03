import MySQLdb
#连接数据库
conn=MySQLdb.connect(host = '127.0.0.1' # 连接名称，默认127.0.0.1 
,user = 'root' # 用户名
,passwd='password' # 密码
,port= 3306 # 端口，默认为3306
,db='student' # 数据库名称
,charset='utf8' # 字符编码
)
cur = conn.cursor() # 生成游标对象 
#=删除语句===================
sql ="UPDATE s SET sname = ‘yu’ WHERE 学号 = ‘20021406’ "
#===================================================
try:
    cur.execute(sql) # 执行插入的sql语句
    conn.commit() # 提交到数据库执行
except:
    conn.rollback()# 如果发生错误则回滚

    conn.close() # 关闭数据库连接