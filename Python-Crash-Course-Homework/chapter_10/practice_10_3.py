# coding:utf-8

username = input("请输入您的名字：")
filename = '../../data/input/guest.txt'
print("\n--- Storing the lines in a list:")
with open(filename, 'w') as f:
    f.write(username + "\n")
