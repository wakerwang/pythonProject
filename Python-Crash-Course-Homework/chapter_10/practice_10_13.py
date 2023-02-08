# coding:utf-8

"""练习10-13：验证用户　最后一个remember_me.py版本假设用户要么已输入用户名，
要么是首次运行该程序。我们应该修改这个程序，以防当前用户并非上次运行该程序的用户。
为此，在greet_user()中打印欢迎用户回来的消息前，询问他用户名是否正确。
如果不对，就调用get_new_username()让用户输入正确的用户名。
"""
import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = f_obj.read()
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """提示用户输入用户名。"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """基于用户名问候用户。"""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


greet_user()