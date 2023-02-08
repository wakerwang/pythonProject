# coding:utf-8

import json


def get_stored_username(filename):
    """如果存储了名字，拿出来"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(filename):
    username = input("请输入用户名称:")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"用户名称为：{username}")


def greet_user(filename):
    username = get_stored_username(filename)
    if username:
        print(f"{username}")
    else:
        get_new_username(filename)


greet_user("username_02.json")
