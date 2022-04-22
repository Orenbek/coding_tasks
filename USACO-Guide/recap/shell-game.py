# coding=utf-8

import sys

sys.stdin = open('shell.in', 'r')
sys.stdout = open('shell.out', 'w')

'''
读取一行 
'''
N = int(input())
count1, count2, count3 = 0, 0, 0
pos = [1, 2, 3]
for _ in range(N):
    a, b, g = map(int, input().split())
    [pos[a - 1], pos[b - 1]] = [pos[b - 1], pos[a - 1]]
    if pos[g - 1] == 1:
        count1 += 1
    elif pos[g - 1] == 2:
        count2 += 1
    elif pos[g - 1] == 3:
        count3 += 1
print(max(count1, count2, count3))
# 12min

