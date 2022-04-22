# coding=utf-8

import sys

# sys.stdin = open('balancing.in', 'r')
# sys.stdout = open('balancing.out', 'w')

N, B = map(int, input().split())
cows = [list(map(int, input().split())) for _ in range(N)]
coord = ({"x": -1, "y": -1}, {"x": -1, "y": 1}, {"x": 1, "y": -1}, {"x": 1, "y": 1})
'''
依次迭代cows中的每个节点 按照左上、右上、左下、右下四个点进行拆分 然后计算每个区域中的牛数量
'''
ret = N


def _max(corx, cory):
    global ret
    q1, q2, q3, q4 = 0, 0, 0, 0
    for x, y in cows:
        if x > corx and y > cory:
            q1 += 1
        if x > corx and y < cory:
            q2 += 1
        if x < corx and y > cory:
            q3 += 1
        if x < corx and y < cory:
            q4 += 1
    top = max(q1, q2, q3, q4)
    if top < ret:
        ret = top


for x, y in cows:
    for _dir in coord:
        corx = x + _dir['x']
        cory = y + _dir['y']
        _max(corx, cory)
print(ret)
