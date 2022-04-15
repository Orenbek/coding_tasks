# coding=utf-8
import sys

sys.stdin = open('gymnastics.in', 'r')
sys.stdout = open('gymnastics.out', 'w')
K, cow_num = map(int, input().split())
matches = [list(map(int, input().split())) for _ in range(K)]

'''
3 4
4 1 2 3
4 1 3 2
4 2 1 3

The consistent pairs of cows are (1,4), (2,4), (3,4), and (1,3).
还是暴力搜索 两层循环
组合问题 但是问题发现也没有那么难 因为这里的pairs必须要每次match中都满足
因此只需要将第一次match中的组合方式列出来 再针对每个组合逐个去查找剩下的match中是不是满足pairs规则

https://www.geeksforgeeks.org/difference-between-find-and-index-in-python/
'''
pair_num = 0
for i in range(cow_num):
    for j in range(i + 1, cow_num):
        fir, sec = matches[0][i], matches[0][j]
        is_pair = True
        for z in range(1, K):
            if matches[z].index(fir) > matches[z].index(sec):
                is_pair = False
        if is_pair:
            pair_num += 1
print(pair_num)
