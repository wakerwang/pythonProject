# -*-coding:utf-8 -*-
# @Time : 2023/2/14 18:49
# @Author : wll
# @File : death_valley_highs_lows.py
# @SoftWare : Pycharm

import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
