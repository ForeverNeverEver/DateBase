from string import Template

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

    while True:
        choose_first = input(T_Choose.substitute())     # 首次登陆时的界面
        if choose_first == 'T' or choose_first == 't':
            role = permissions.getRole()
            break
        elif choose_first == 'E' or choose_first == 'e':
            exit(0)
        else:
            print("输入错误，请重新输入")

    while True:
        choose_log = input(T_login)
        if choose_log == 'C' or choose_log == 'c':
            state = permissions.login(role)
            break
        elif choose_log == 'E' or choose_log == 'e':
            exit(0)
        else:
            print("输入错误，请重新输入")

    if role == '管理员':
        pass
    if role == '教务人员':
        pass
    if role == '学生':
        pass
    if role == '教师':
        pass
