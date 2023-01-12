#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
王者荣耀角色管理系统；
1、实现添加、修改、查看、删除角色、退出系统功能
"""
from time import sleep

print("欢迎进入王者荣耀角色管理系统~~~~~~")
all_role = []
while True:
    choice = input("请选择功能：\n1.添加角色 \n2.修改角色 \n3.查看角色 \n4.删除角色 \n5.显示所有角色 \n6.退出系统\n")
    if choice == "1":
        print("欢迎使用'添加角色'功能：")
        role_name = input("\t请输入角色名称：")
        role_sex = input("\t请输入角色性别：")
        role_job = input("\t请输入角色职业：")
        role = [role_name, role_sex, role_job]
        all_role.append(role)
        print("\t角色{}已成功添加".format(role_name))
    elif choice == "2":
        print("欢迎使用'修改角色'功能：")
        update_role_name = input("\t请输入需要修改的角色名称：")
        for k in all_role:
            if update_role_name in k:
                print("\t当前输入的角色'{}'存在于系统中！".format(update_role_name))
                k[0] = input("\t请输入新的角色名称：")
                k[1] = input("\t请输入新的角色性别：")
                k[2] = input("\t请输入新的角色职业：")
                print("\t当前角色'{}'已修改成功！".format(update_role_name))
            else:
                print("\t当前输入的角色'{}'不存在于系统中，无法修改！".format(
                    update_role_name))  # 所查的名称不是第一个元素时，会走该分支，解决方法参考elif choice == "2"
    elif choice == "3":
        print("欢迎使用'查询角色'功能：")
        select_role_name = input("\t请输入要查询的角色名称：")
        all_role_name = []
        for j in all_role:
            all_role_name.append(j[0])
        if select_role_name in all_role_name:
            print("\t当前输入的角色'{}'存在于系统中：".format(select_role_name))
            print("\t{}{}{}".format("角色名称".center(10), "角色性别".center(10), "角色职业".center(10)))
            for js in all_role:
                if select_role_name in js:
                    print("\t", js[0].center(10), js[1].center(10), js[2].center(10))
        else:
            print("\t当前输入的角色'{}'不存在于系统中！".format(select_role_name))
    elif choice == "4":
        print("欢迎使用'删除角色'功能：")
        delete_role_name = input("\t请输入要删除的角色名称：")
        for j in all_role:
            if delete_role_name in j:
                print("\t当前输入的角色'{}'存在于系统中！".format(delete_role_name))
                ask = input("是否确认删除（请输入y/n）？")
                if ask.upper() == "Y":
                    all_role.remove(j)  # 同样的问题，如果出现同名的角色，则会出现删除不干净的情况，可以使用while循环解决，此处略
                    print("\t角色'{}'已成功被删除".format(delete_role_name))
                else:
                    pass
            else:
                print("\t当前输入的角色'{}'不存在于系统中！".format(delete_role_name))  # 所查的名称不是第一个元素时，会走该分支，解决方法参考elif choice == "3"
    elif choice == "5":
        print("欢迎使用'查看所有角色'功能：")
        print(all_role)
        print("{}{}{}".format("角色名称".center(10), "角色性别".center(10), "角色职业".center(10)))
        for i in all_role:
            print(i[0].center(10), i[1].center(10), i[2].center(10))
    elif choice == "6":
        print("正在退出系统~~~")
        sleep(1)
        print("退出成功！")
        break
    else:
        print("输入错误，请重新选择！")
