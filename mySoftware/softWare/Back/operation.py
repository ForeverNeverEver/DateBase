import MySQLdb
from string import Template
sql_T = Template("""INSERT INTO \
        $tableName(姓名, 性别, 民族, 生日, 家庭住址, 电话)
        VALUES ('$Name', '$Gender', '$nation', '$date', '$local', '$PhoneNumber')""")


class Insert:
    # 获取操作角色
    def __init__(self):
        opDict = {'tableName': None, 'Name': None, 'Gender': None,\
                  'nation': None, 'date': None, 'local': None, 'Phone': None}
        user = input("请输入用户名")
        password = input("请输入密码")
        # 打开数据库连接
        connect = MySQLdb.connect('localhost', user, password, 'JWGL', charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = connect.cursor()
        try:
            # 执行sql语句
            cursor.execute(sql_T.substitute())
            # 提交到数据库执行
            connect.commit()
        finally:
            # Rollback in case there is any error
            connect.rollback()

        # 关闭数据库连接
        connect.close()
