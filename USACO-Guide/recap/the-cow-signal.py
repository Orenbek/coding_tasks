# coding=utf-8

import sys

sys.stdin = open('cowsignal.in', 'r')
sys.stdout = open('cowsignal.out', 'w')

N, M, expand = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
for i in range(len(matrix)):
    for _ in range(expand):
        for j in range(M):
            print(matrix[i][j] * expand, end='')
        print()
