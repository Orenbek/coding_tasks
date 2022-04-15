# coding=utf-8
import sys

sys.stdin = open('triangles.in', 'r')
sys.stdout = open('triangles.out', 'w')
N = int(input())
coors = [list(map(int, input().split())) for _ in range(N)]
'''
针对每个坐标 逐个的查找让他和x或者是y轴平行的坐标
再针对查找到的坐标计算面积算最大值
'''
max_val = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        at_x = coors[i][1] == coors[j][1]
        at_y = coors[i][0] == coors[j][0]
        if at_x:
            for z in range(j + 1, N):
                zi_y = coors[i][0] == coors[z][0]
                # z点和i点同在y轴
                zj_y = coors[j][0] == coors[z][0]
                # z点和j点同在y轴
                if zi_y:
                    max_val = max(max_val, abs(coors[i][0] - coors[j][0]) * abs(coors[i][1] - coors[z][1]))
                if zj_y:
                    # z点和j点同在y轴
                    max_val = max(max_val, abs(coors[i][0] - coors[j][0]) * abs(coors[j][1] - coors[z][1]))
        if at_y:
            for z in range(j + 1, N):
                zi_x = coors[i][1] == coors[z][1]
                # z点和i点同在x轴
                zj_x = coors[j][1] == coors[z][1]
                # z点和j点同在y轴
                if zi_x:
                    max_val = max(max_val, abs(coors[i][1] - coors[j][1]) * abs(coors[i][0] - coors[z][0]))
                if zj_x:
                    max_val = max(max_val, abs(coors[i][1] - coors[j][1]) * abs(coors[j][0] - coors[z][0]))
print(max_val)
