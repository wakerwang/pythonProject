# coding:utf-8

from name_function import get_formatted_name

print("Enter 'q' at any time to quit!")
while True:
    first = input("Please give me the first name:")
    if first == 'q':
        break
    last = input("Please give me the last name:")
    if first == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name:{formatted_name}")

