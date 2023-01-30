# coding:utf-8

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.greet_user()

    def describe_user(self):
        print(f"姓名：{self.first_name}{self.last_name}")

    def greet_user(self):
        print(f"你好，{self.first_name}{self.last_name}")





class Admin(User):
    def __init__(self):
        super(Admin, self).__init__()