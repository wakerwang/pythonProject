# coding:utf8

import calendar
import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta


class DateTimeUtil():

    def get_cur_month(self):
        # 获取当前月
        return datetime.now().strftime("%Y-%m")

    def get_last_month(self, number=1):
        # 获取前几个月
        month_date = datetime.now().date() - relativedelta(months=number)
        return month_date.strftime("%Y-%m")

    def get_next_month(self, number=1):
        # 获取后几个月
        month_date = datetime.now().date() + relativedelta(months=number)
        return month_date.strftime("%Y%m")

    def get_cur_month_start(self):
        # 获取当前月的第一天
        month_str = datetime.now().strftime('%Y-%m')
        return '{}-01'.format(month_str)

    def get_cur_month_end(self):
        # 获取当前月的最后一天
        '''
        param: month_str 月份，2021-04
        '''
        # return: 格式 %Y-%m-%d

        month_str = datetime.now().strftime('%Y-%m')
        year, month = int(month_str.split('-')[0]), int(month_str.split('-')[1])
        end = calendar.monthrange(year, month)[1]
        return '{}-{}-{}'.format(year, month, end)

    def get_last_month_start(self, month_str=None):
        # 获取上一个月的第一天
        '''
        param: month_str 月份，2021-04
        '''
        # return: 格式 %Y-%m-%d
        if not month_str:
            month_str = datetime.now().strftime('%Y-%m')
        year, month = int(month_str.split('-')[0]), int(month_str.split('-')[1])
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
        return '{}-{}-01'.format(year, month)

    def get_next_month_start(self, month_str=None):
        # 获取下一个月的第一天
        '''
        param: month_str 月份，2021-04
        '''
        # return: 格式 %Y-%m-%d
        if not month_str:
            month_str = datetime.now().strftime('%Y-%m')
        year, month = int(month_str.split('-')[0]), int(month_str.split('-')[1])
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        return '{}-{}-01'.format(year, month)

    def get_last_month_end(self, month_str=None):
        # 获取上一个月的最后一天
        '''
        param: month_str 月份，2021-04
        '''
        # return: 格式 %Y-%m-%d
        if not month_str:
            month_str = datetime.now().strftime('%Y-%m')
        year, month = int(month_str.split('-')[0]), int(month_str.split('-')[1])
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
        end = calendar.monthrange(year, month)[1]
        return '{}-{}-{}'.format(year, month, end)

    def get_next_month_end(self, month_str=None):
        # 获取下一个月的最后一天
        '''
        param: month_str 月份，2021-04
        '''
        # return: 格式 %Y-%m-%d
        if not month_str:
            month_str = datetime.now().strftime('%Y-%m')
        year, month = int(month_str.split('-')[0]), int(month_str.split('-')[1])
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
        end = calendar.monthrange(year, month)[1]
        return '{}-{}-{}'.format(year, month, end)

    def auto_get_run_date(self, today_str=None):
        if today_str is not None:
            today_str = today_str
        else:
            today_str = datetime.now().strftime('%Y%m%d')
        this_month_str = datetime.now().strftime('%Y%m')
        next_month = self.get_next_month(1)
        last_month = self.get_next_month(-1)
        if today_str <= this_month_str + "26":
            timemin = last_month + "26"
            timemax = this_month_str + "25"
        else:
            timemin = this_month_str + "26"
            timemax = next_month + "25"
        return timemin, timemax


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        print(DateTimeUtil().auto_get_run_date(args[1]))
    else:
        print(DateTimeUtil().auto_get_run_date())
