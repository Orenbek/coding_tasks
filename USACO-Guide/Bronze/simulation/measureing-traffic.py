# coding=utf-8

import sys

sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

N = int(input())

road = [[val if i == 0 else int(val) for i, val in enumerate(input().split())] for _ in range(N)]

low, high = -float('inf'), float('inf')
# 从后往前来一遍
for index in range(N - 1, -1, -1):
    [road_type, min_val, max_val] = road[index]
    if road_type == 'none':
        low = max(low, min_val)
        high = min(high, max_val)
    elif road_type == 'on':
        low -= max_val
        high -= min_val
        # Set to zero if low becomes negative
        low = max(0, low)
    else:
        low += min_val
        high += max_val
print(low, high)

low, high = -float('inf'), float('inf')
# 从前往后来一遍
for road_type, min_val, max_val in road:
    if road_type == 'none':
        low = max(low, min_val)
        high = min(high, max_val)
    elif road_type == 'on':
        low += min_val
        high += max_val
    else:
        low -= max_val
        high -= min_val
        low = max(0, low)
print(low, high)
