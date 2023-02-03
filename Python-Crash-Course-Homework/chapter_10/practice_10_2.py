# coding:utf-8

filename = '../../data/input/learning_python.txt'
print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()
for line in lines:
    print(line.replace("Python","C").rstrip())
