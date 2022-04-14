# coding=utf-8
import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

N = int(input())
words = [input().split() for _ in range(N)]
all_alpha = 'abcdefghijklmnopqrstuvwxyz'
total_map = [0 for _ in all_alpha]
alpha_map = {val: index for index, val in enumerate('abcdefghijklmnopqrstuvwxyz')}

for word1, word2 in words:
    record1, record2 = [0 for _ in all_alpha], [0 for _ in all_alpha]
    for w in word1:
        record1[alpha_map[w]] += 1
    for w in word2:
        record2[alpha_map[w]] += 1
    for index in range(26):
        record1[index] = max(record1[index], record2[index])
        total_map[index] += record1[index]
for item in total_map:
    print(item)
