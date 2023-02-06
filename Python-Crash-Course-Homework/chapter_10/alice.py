# coding:utf-8

filename='alice.txt'

try:
    with open(filename,encoding='utf-8') as f:
        contents=f.read()
except FileNotFoundError:
    print("No file found!")
else:
    words=contents.split()
    num_words=len(words)
    print(num_words)