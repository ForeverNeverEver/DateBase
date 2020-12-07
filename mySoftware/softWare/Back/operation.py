import MySQLdb
from string import Template

T_INS_S = Template("""INSERT INTO # 学生插入语句模板
        $tableName(学号, 姓名, 性别, 民族, 生日, 家庭住址, 电话, 专业代码, 类别)
        VALUES ($ID, $Name, $Gender, $nation, $birthdate, $local, $PhoneNumber, $zhuanyeID, $leibie)""")

T_INS_T = Template("""INSERT INTO # 学生插入语句模板
        $tableName(教师号, 姓名, 性别, 民族, 生日, 家庭住址, 电话, 职称, 学历)
        VALUES ($ID, $Name, $Gender, $nation, $birthdate, $local, $PhoneNumber, $zc, $xl)""")

ins_dict = {'tableName': None, 'ID': None, 'Name': None, 'Gender': None,
            'nation': None, 'birthdate': None, 'local': None, 'Phone': None}

T_DEL_S = Template("""DELETE FROM # 删除语句模板
$tableName WHERE 姓名 = $name AND 学号 = $ID""")

T_DEL_T = Template("""DELETE FROM # 删除语句模板
$tableName WHERE 姓名 = $name AND 教师号 = $ID""")

del_dict = {'tableName': None, 'name': None, 'ID': None}

T_SEL = Template("""SELECT $column_name # 查询语句模板
                    FROM $tableName""")

sel_dict = {'column_name': None, 'tableName': None}

T_UPD = Template("""UPDATE $tableName
                    SET $column=$value
                    WHERE $key=$key_value""")

upd_dict = {'tableName': None, 'column': None, 'value': None, 'key': None, 'key_value': None}

Tip_input = Template("请输入 $all")


def Connect(op: dict, statement):    # 链接数据库
    # 获取操作角色
    # password = input("请输入数据库密码")
    try:    # 打开数据库连接
        connect = MySQLdb.connect('localhost', 'root', 'MlwithYx0109', 'JWGL', charset='utf8')
        # 使用cursor()方法获取操作游标
        cursor = connect.cursor()
        # 执行sql语句
        cursor.execute(statement.substitute(op))
        final = cursor.fetchone()
        # 提交到数据库执行
        connect.commit()
    except Exception as e:
        print(e)
        # Rollback in case there is any error
        connect.rollback()
    # 关闭数据库连接
    connect.close()
    return final


def Insert(role: str, op: dict = ins_dict):     # 增
    for item in op():
        value = input(Tip_input.substitute(all=item))
        op.update({item: value})
    Connect(op, role)


def Delete(role: str, op: dict = del_dict):      # 删
    print("现在开始删除记录")
    for item in op():
        value = input(Tip_input.substitute(all=item))
        op.update({item: value})
    Connect(op, role)


def Select(op: dict = sel_dict):       # 查
    for item in op:
        value = input(Tip_input.substitute(all=item))
        op.update({item: value})
    Connect(op, T_SEL)


def Update(op: dict = upd_dict):       # 改
    key = input("请输入表名")
    op.update({'tableName': key})
    key = input("请输入需要更改的项目主键名称")
    op.update({'key': key})
    key = input("请输入需要更改的项目主键名称")
    op.update({'key_value': key})
    key = input("请输入需要更改的项目名称")
    op.update({'column': key})
    op.update({'column': key})
    key = input("请输入需要更改的项目名称")
    op.update({'column': key})
    key = input("您需要将其值更改为：")
    op.update({'value': key})
    key = input("请输入需要更改的项目名称")
    op.update({'column': key})
    Connect(op, T_UPD)
