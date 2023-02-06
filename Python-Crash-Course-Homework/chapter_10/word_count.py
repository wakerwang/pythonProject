# coding:utf-8

def count_words(filename):
    try:
        with open(filename,encoding='utf-8') as f:
            contents=f.read()
    except FileNotFoundError:
        print("File Not Found!")
    else:
        words=len(contents)
        print(f"{filename} have {words} words")


filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)