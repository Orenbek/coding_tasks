# coding=utf-8

N = int(input())
arr = list(map(int, input().split()))
'''
1≤i≤j≤N
暴力搜索
两层for循环
每层循环里面 对当前花瓣数量进行统计
1 1 2 3
'''
res = 0
for i in range(N):
    cur_sum = 0
    for j in range(i, N):
        cur_sum += arr[j]
        if cur_sum / (j - i + 1) in arr[i:j + 1]:
            res += 1
print(res)
