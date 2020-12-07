from string import Template
import MySQLdb
import hashlib

get_role = Template("请键入您的身份:\nA:管理员\nH:教务人员\nT:教师\nS:学生\n")
role = {'A': '管理员', 'H': '教务人员', 'T': '教师', 'S': '学生'}
role_login = Template("您已以$role身份登录")


def login(op_role: str):

    login_role = op_role
    password = input("请输入数据库密码")
    conn = MySQLdb.connect('localhost', 'root', password, 'JWGL', charset='utf8')
    # 接收用户输入
    name = input("请输入用户名:")
    pwd = input("请输入密码:")
    res = [name]
    pwd2 = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    # 根据用户名查询密码

    sql = 'select 密码 from 用户权限 where 用户名=%s'
    cus1 = conn.cursor()
    cus1.execute(sql, res)
    psw = cus1.fetchall()
    if psw == ():
        print("用户名错误")
        state = False
    elif psw[0][0] == pwd2:
        print(role_login.substitute(role=login_role))
        state = True
    else:
        print("密码错误")
        state = False
    conn.commit()
    cus1.close()
    conn.close()

    return state


def getRole():
    role_choose = input(get_role.substitute())  # 取得的值为大写字母
    return role.get(role_choose)


def create_user():
    name = input("用户名:")
    while True:
        pwd1 = input("密码:")
        pwd2 = input("请再输入一遍密码:")
        if pwd1 == pwd2:
            break
        else:
            print("两次密码不一致！")
    try:
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="123456", db="Python3", charset="utf8")
        cus1 = conn.cursor()
        sql = "insert into 用户权限(姓名,密码) values(%s, %s)"
        pwd = hashlib.sha1(pwd2.encode("utf-8")).hexdigest()
        print(pwd)
        res = [name, pwd]
        print(res)
        cus1.execute(sql, res)
        conn.commit()
        cus1.close()
        conn.close()
    except Exception as e:
        print(e)
    else:
        print("新用户创建成功")
