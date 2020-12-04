from string import Template

get_role = Template("请键入您的身份:\nA:管理员\nH:教务人员\nT:教师\nS:学生\n")
role = {'A': '管理员', 'H': '教务人员', 'T': '教师', 'S': '学生'}
role_login = Template("您已以 $role 身份登录")

TeacherMenu = Template("教师选单：\n")
TeacherOP = {'C': '创建个人资料'}


def login():

    login_role = getRole()
    print(role_login.substitute(login_role))
    return login_role


def getRole():
    role_choose = input(get_role.substitute())
    return role.get(role_choose)


if __name__ == '__main__':
    key = login()
    if key == 'A':
        print()
    elif key == 'H':
        print()
    elif key == 'T':
        print()
    elif key == 'S':
        print()
