# coding=utf-8
import sys
from functools import reduce

sys.stdin = open('lifeguards.in', 'r')
sys.stdout = open('lifeguards.out', 'w')

N = int(input())
guards = [list(map(int, input().split())) for _ in range(N)]
time_map = [0 for _ in range(1000)]
total_time = 0
# 这道题很巧妙的利用了一个数组来表示cover住的时间，不然这道题还是比较麻烦的
for [start, end] in guards:
    for j in range(start, end):
        time_map[j] += 1
for [start, end] in guards:
    for j in range(start, end):
        time_map[j] -= 1
    total_time = max(total_time, reduce(lambda a, b: a + 1 if b != 0 else a, time_map, 0))
    for j in range(start, end):
        time_map[j] += 1
print(total_time)
