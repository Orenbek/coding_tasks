"""
ID: orenbek1
LANG: PYTHON3
TASK: friday
"""
# coding=utf-8

import sys

sys.stdin = open('friday.in', 'r')
sys.stdout = open('friday.out', 'w')


def is_leap_year(year):
    return (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


months_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dates_counts = [0, 0, 0, 0, 0, 0, 0]
N = int(input())
year_first_date = 0
pre_year_days = 0
for i in range(N):
    leap_year = is_leap_year(1900 + i)
    year_first_date = 0 if i == 0 else (year_first_date + pre_year_days) % 7
    '''
    这里涉及到 模运算 模运算的相关公式我整理到了onenote中 注意回忆学习记录
    '''
    pre_year_days = 366 if leap_year else 365
    cur_sum = 0
    for index, val in enumerate(months_days):
        dates_counts[(year_first_date + cur_sum + 13 - 1) % 7] += 1
        cur_sum += 29 if leap_year and index == 1 else val
for i in range(-2, 5):
    # print Saturday, Sunday, Monday, Tuesday, ..., Friday.
    print(dates_counts[i], end=" " if i != 4 else "\n")
# 这道题整整花了我三四个小时时间
