# coding:utf-8

from practice_9_12_02 import Admin

eric=Admin('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts'
]
eric.privileges.privileges=eric_privileges

eric.privileges.show_privileges()
