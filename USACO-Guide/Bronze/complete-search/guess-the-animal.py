# coding=utf-8

import sys

sys.stdin = open('guess.in', 'r')
sys.stdout = open('guess.out', 'w')

'''
寻找最长子串问题
两个for循环 然后俩俩相减 看能减掉最多的元素的那一对就是最长的数量
'''

N = int(input())
animals = [[val for index, val in enumerate(input().split()) if index >= 2] for _ in range(N)]
max_len = 0
for i in range(N):
    for j in range(i + 1, N):
        # 注意j的范围
        # another way, len([i for i in animals[i] if i in animals[j]])
        common_len = len(set(animals[i]).intersection(set(animals[j])))
        max_len = max(max_len, common_len)
print(max_len + 1)
