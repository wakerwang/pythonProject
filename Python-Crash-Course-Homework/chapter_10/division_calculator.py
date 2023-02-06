# coding:utf-8

print("Give me two numbers, and I'll divide them")
print("Enter 'q' to exit!")

while True:
    first_munber = input("First number:\n")
    if first_munber.lower() == 'q':
        break
    second_num = input("Second number:\n")
    if second_num.lower() == 'q':
        break
    try:
        res = int(first_munber) / int(second_num)
    except ZeroDivisionError:
        print("The second number can't be Zore!")
    else:
        print(f"The result is {res}")
