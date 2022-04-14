# coding=utf-8
import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

N = int(input())
cows = [int(input()) for _ in range(N)]

cur_min_sum = float('inf')
for index in range(N):
    cur_sum = 0
    for i in range(N):
        cur_sum += ((i - index + N) % N) * cows[i]
        # 本题关键点就在于理解题意 并且 (i - index + N) % N 这个关系式写对
    cur_min_sum = min(cur_sum, cur_min_sum)
print(cur_min_sum)
