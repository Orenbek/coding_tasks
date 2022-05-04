# coding=utf-8
import sys

sys.stdin = open('pails.in', 'r')
sys.stdout = open('pails.out', 'w')

fir, sec, third = map(int, input().split())

max_num = 0
for i in range(third // fir + 1):
    amount = fir * i + ((third - fir * i) // sec) * sec
    max_num = max(amount, max_num)
for i in range(third // sec + 1):
    amount = sec * i + ((third - sec * i) // fir) * fir
    max_num = max(amount, max_num)
print(max_num)
