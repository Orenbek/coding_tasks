# coding=utf-8
import sys

# sys.stdin = open('cownomics.in', 'r')
# sys.stdout = open('cownomics.out', 'w')
sys.stdin = open('./test/2.in', 'r')
N, M = map(int, input().split())
spotty = [list(input()) for _ in range(N)]
plain = [list(input()) for _ in range(N)]
'''
逐个index去比较
'''
index = -1

for i in range(M):
    spo = set([spotty[x][i] for x in range(N)])
    if spo == {'A', 'G'}:
        pla = set([plain[x][i] for x in range(N)])
        if pla == {'C'}:
            index = i
            break
print(index)
