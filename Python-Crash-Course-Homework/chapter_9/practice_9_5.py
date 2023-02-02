# coding:utf8

class User:
    def __init__(self, first_name, last_name, attemps, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.attemps = attemps
        self.login_attempts = login_attempts
        self.greet_user()

    def describe_user(self):
        print(f"姓名：{self.first_name}{self.last_name},登陆次数为：{self.login_attempts}")

    def greet_user(self):
        print(f"你好，{self.first_name}{self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attemps(self):
        self.login_attempts = 0


user = User("Wang", "longlong", 0, 0)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

user.describe_user()
user.reset_login_attemps()
user.describe_user()
