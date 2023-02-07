# coding:utf-8

filename = '../../data/input/programming_poll.txt'

while True:
    try:
        first_number = input("请输入第一个数字:")
        if first_number.lower() == 'q':
            break
        second_number = input("请输入第二个数字:")
        if second_number.lower() == 'q':
            break
        res = int(first_number) + int(second_number)
    except ValueError:
        print("输入的数字必须能转换为数字！")
    else:
        print(res)
