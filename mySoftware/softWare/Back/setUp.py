import MySQLdb


def setUpDB():
    # Tpassword = input("请输入数据库密码")
    conn = MySQLdb.connect("localhost", 'root', 'MlwithYx0109', "JWGL", charset='utf8')    # 打开数据库链接
    cursor = conn.cursor()    # 开启游标
    with open('setUp.sql', 'r', encoding='utf-8') as source:      # 打开文件命名为source
        sql_list = source.read().split(';')[:-1]
        for item in sql_list:
            if '\n' in item:
                # 替换空行为1个空格
                item = item.replace('\n', ' ')
            # 判断多个空格时
            if '    ' in item:
                # 替换为空
                item = item.replace('    ', '')
            cursor.execute(item)
            print("执行成功sql语句: %s" % item)
    source.close()    # 关闭source文件
    cursor.close()    # 关闭游标
    conn.close()      # 关闭数据库链接


if __name__ == '__main__':
    setUpDB()
