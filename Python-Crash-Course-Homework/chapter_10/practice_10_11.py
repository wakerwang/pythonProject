# coding:utf-8

"""
练习10-11：喜欢的数　编写一个程序，提示用户输入喜欢的数，并使用json.dump()将这个数存储到文件中。
再编写一个程序，从文件中读取这个值，并打印如下所示的消息。
I know your favorite number! It's _____.
"""
import json


def input_number(filename):
    try:
        with open(filename, 'w') as f:
            number = input("请输入一个你喜欢的数字:")
            json.dump(number, f)
    except FileNotFoundError:
        print("文件不存在：")
        with open(filename, 'w') as f:
            number = input("请输入一个你喜欢的数字:")
            json.dump(number, f)
    else:
        print(f"您输入的数字是{number}")


def output_number(filename):
    try:
        with open(file=filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        print("文件不存在")
    else:
        print(f"数字是:{number}")


filename = "num.json"
input_number(filename)
output_number(filename)
