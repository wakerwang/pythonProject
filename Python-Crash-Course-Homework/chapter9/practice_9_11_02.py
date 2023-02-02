# coding:utf-8

from practice_9_11_01 import User, Privileges, Admin

eric = Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.privileges.show_privileges()
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts'
]


eric.privileges.privileges=eric_privileges

eric.describe_user()
eric.privileges.show_privileges()