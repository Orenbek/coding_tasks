# coding=utf-8

import sys
from functools import reduce

sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")

rows, cols, k = map(int, input().split())
matrix = [input() for _ in range(rows)]
for index in range(rows):
    for _ in range(k):
        print(reduce(lambda a, b: a + b * k, matrix[index], ''))

'''
或者是下面这种方式
'''
# for i in range(k * rows):
#     for j in range(k * cols):
#         print(g[i // k][j // k], end='')
# print()
