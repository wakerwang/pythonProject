# coding:utf-8

filename = '../../data/input/guest_book.txt'

username = input("请输入您的名字：")
with open(filename, 'w') as f:
    while True:
        if username.lower() != 'quit':
            print(f"你好呀，{username}")
            f.write(username + "\n")
            username = input("请输入您的名字：")
        else:
            print("再见！")
            break
