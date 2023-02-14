# -*-coding:utf-8 -*-
# @Time : 2023/2/14 16:58
# @Author : wll
# @File : die_visual.py
# @SoftWare : Pycharm

from die import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

die1 = Die()
die2 = Die()

results = []

for roll_num in range(100):
    result = die1.roll() + die2.roll()
    results.append(result)

# 分析结果
freqs = []
m = die1.num_sides + die2.num_sides
for value in range(2, m + 1):
    freq = results.count(value)
    freqs.append(freq)

# 可视化
x_values = list(range(2, m + 1))
data = [Bar(x=x_values, y=freqs)]

x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}

my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
