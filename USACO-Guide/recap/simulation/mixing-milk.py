# coding=utf-8

import sys

sys.stdin = open('mixmilk.in', 'r')
sys.stdout = open('mixmilk.out', 'w')

cans = [list(map(int, input().split())) for _ in range(3)]
for i in range(100):
    [capacity1, vol1] = cans[i % 3]
    [capacity2, vol2] = cans[(i + 1) % 3]
    if capacity2 - vol2 > vol1:
        cans[(i + 1) % 3][1] = vol2 + vol1
        cans[i % 3][1] = 0
    else:
        cans[(i + 1) % 3][1] = capacity2
        cans[i % 3][1] = vol1 - (capacity2 - vol2)
    '''
    optimized version
    更加简洁 数学关系更加明确
    amt = min(cans[i % 3][0], cans[(i + 1) % 3][0] - cans[(i + 1) % 3][1])
    cans[(i + 1) % 3][1] += amt
    cans[i % 3][1] -= amt
    '''
for item in cans:
    print(item[1])
