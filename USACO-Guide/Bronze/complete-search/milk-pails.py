# coding=utf-8

import sys

sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

fir, sec, third = map(int, input().split())

max_num = 0
for i in range((third // fir) + 1):
    total = ((third - i * fir) // sec) * sec + i * fir
    max_num = max(max_num, total)
for i in range((third // sec) + 1):
    total = ((third - i * sec) // fir) * fir + i * sec
    max_num = max(max_num, total)
print(max_num)
