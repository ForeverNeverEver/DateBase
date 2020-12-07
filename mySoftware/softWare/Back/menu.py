from string import Template
import operation
import permissions

T_Welcome = Template(
    """
    
    ——————————————————————————————————————欢迎使用教务管理系统——————————————————————————————————————
    
    """
)

T_Choose = Template(
    """
    [T]进入系统
    [E]退出系统
    """
)

T_login = (
    """
    [C]登录系统
    [E]退出系统
    """
)

T_Admin_choose = Template(
    """
    [A]创建用户
    [B]删除用户
    [C]到上一级选单
    [D]退出程序
    """
)

T_JW_choose = Template(
    """
    [A]增加老师
    [B]增加学生
    [C]删除老师
    [D]删除学生
    [E]修改老师及学生信息
    [F]查找老师及学生信息
    [G]设置课程
    [H]管理专业
    [I]到上一级选单
    [J]退出程序
    """
)

T_Teacher_choose = Template(
    """
    [A]增加学生
    [B]删除学生
    [C]查询学生
    [D]修改学生
    [E]使用教室
    [F]到上一级选单
    [G]退出程序
    """
)

T_student_choose = Template(
    """
    [A]查询学生
    [B]到上一级选单
    [C]退出程序
    """
)

role = str


def run():
    welcome()


def welcome():
    while True:
        choose_first = input(T_Choose.substitute())     # 首次登陆时的界面
        if choose_first == 'T' or choose_first == 't':
            global role
            role = permissions.getRole()
            login_first(role)
            break
        elif choose_first == 'E' or choose_first == 'e':
            exit(0)
        else:
            print("输入错误，请重新输入")


def login_first(op: str):
    while True:
        choose_log = input(T_login)
        if choose_log == 'C' or choose_log == 'c':
            state = permissions.login(op)
            if not state:
                print("用户名或密码错误！\n请检查您的用户名和密码，或联系管理员创建用户")
            if state:
                chooseTab()
                break
        elif choose_log == 'E' or choose_log == 'e':
            exit(0)
        else:
            print("输入错误，请重新输入")


def chooseTab():
    if role == '管理员':
        while True:
            choose = input(T_Admin_choose)
            if choose == 'A' or choose == 'a':    # [A]创建用户
                permissions.create_user()
                chooseTab()
                break
            elif choose == 'B' or choose == 'b':    # [B]删除用户
                sql = Template('DELETE FROM 用户权限 WHERE 用户名 = $name')
                user = input("请输入要删除的用户的用户名")
                operation.Connect({'name': user}, sql)
                print("已删除\n用户名："+user+"的用户")
                chooseTab()
                break
            elif choose == 'C' or choose == 'c':    # [C]到上一级选单
                break
            elif choose == 'D' or choose == 'd':    # [D]退出程序
                exit(0)

    elif role == '教务人员':
        while True:
            choose = input(T_JW_choose)
        # [A]增加老师
            if choose == 'A' or choose == 'a':
                operation.Insert('T_INS_T')
                break
        # [B]增加学生
            if choose == 'B' or choose == 'b':
                operation.Insert('T_INS_S')
                break
        # [C]删除老师
            if choose == 'C' or choose == 'c':
                operation.Delete('T_DEL_T')
                break
        # [D]删除学生
            if choose == 'D' or choose == 'd':
                operation.Delete('T_DEL_S')
                break
        # [E]修改老师及学生信息
            if choose == 'E' or choose == 'e':
                operation.Update('T_UPD')
                break
        # [F]查找老师及学生信息
            if choose == 'F' or choose == 'f':
                operation.Select('T_SEL')
                break
        # [G]设置课程
            if choose == 'G' or choose == 'g':
                num = input("请输入课号")
                name = input("请输入课名")
                time = input("请输入总学时")
                dg = input("请输入教学大纲")
                lx = input("请输入课程类型")
                sqlg = Template("""insert into 课程(课号, 课名, 总学时, 教学大纲, 课程类型, 课程简介) 
                                values($ID, $name, $time, $dg, $lx, NULL)""")
                operation.Connect({'ID': num, 'name': name, 'time': time, 'dg': dg, 'lx': lx}, sqlg)
                break
        # [H]管理专业
            if choose == 'H' or choose == 'h':
                num = input("请输入专业代号")
                name = input("请输入专业名称")
                sqlh = Template("""insert into 专业(专业代号, 名称)
                                values ($ID, $name)""")
                operation.Connect({'ID': num, 'name': name}, sqlh)
                break
        # [I]到上一级选单
            if choose == 'I' or choose == 'i':
                break
        # [J]退出程序
            if choose == 'J' or choose == 'j':
                exit(0)

    elif role == '学生':
        while True:
            choose = input(T_student_choose)
            # [A]查询学生
            if choose == 'A' or choose == 'a':
                operation.Select('T_SEL')
                break
        # [B]到上一级选单
            if choose == 'B' or choose == 'b':
                break
        # [C]退出程序
            if choose == 'A' or choose == 'a':
                exit(0)
    elif role == '教师':
        while True:
            choose = input(T_Teacher_choose)
            # [A]增加学生
            if choose == 'A' or choose == 'a':
                operation.Insert('T_INS_S')
                break
            # [B]删除学生
            if choose == 'B' or choose == 'b':
                operation.Delete('T_DEL_S')
                break
            # [C]查询学生
            if choose == 'C' or choose == 'c':
                operation.Select('T_SEL')
                break
            # [D]修改学生
            if choose == 'D' or choose == 'd':
                operation.Update('T_UPD')
                break
            # [E]使用教室
            if choose == 'E' or choose == 'e':
                num = input("请输入专业代号")
                cnum = input("请输入专业名称")
                week = input("请输入周")
                cs =input("请输入节数")
                sqlh = Template("""insert into 教室(教室号, 教学班号, 周, 节)
                                values ($ID, $cID, $week, $num)""")
                operation.Connect({'ID': num, 'cID': cnum, 'week': week, 'num': cs}, sqlh)
                break
            # [F]到上一级选单
            if choose == 'F' or choose == 'f':
                exit(0)
            # [G]退出程序
    else:
        print("输入错误请重新输入")
