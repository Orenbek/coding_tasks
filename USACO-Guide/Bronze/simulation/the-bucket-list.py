# coding=utf-8

import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")
# 本题是计算最少需要多少奶桶

cows = [list(map(int, input().split())) for _ in range(int(input()))]  # [start, end, bucket_num][]
start_milk_in_order = sorted(cows, key=lambda x: x[0])  # cows.sort是原地排序 sorted是返回新的数组
end_milk_in_order = sorted(cows, key=lambda x: x[1])
start_milk_index = 0
end_milk_index = 0
total_bucket_num = 0
remaining_bucket_num = 0
'''
我们不需要关心奶牛取的是第几个桶，因为规则上说了每次是取出编号最小的bi个桶
因此我们只需要记录当前剩余多少个桶 remaining_bucket_num，以及我们一共有多少个桶 total_bucket_num 即可。
这个题和 speeding-ticket 那个题一样 都是两个list中判断元素哪个最小并且依次读取
'''
while True:
    if start_milk_index == end_milk_index == len(cows):
        # 终止条件是等于 len(cows) 不是 len(cows) - 1
        break

    if start_milk_index < len(cows) and start_milk_in_order[start_milk_index][0] < end_milk_in_order[end_milk_index][1]:
        # start milking 注意⚠️需要判断是否越界
        if start_milk_in_order[start_milk_index][2] < remaining_bucket_num:
            remaining_bucket_num -= start_milk_in_order[start_milk_index][2]
        else:
            total_bucket_num += start_milk_in_order[start_milk_index][2] - remaining_bucket_num
            remaining_bucket_num = 0
        start_milk_index += 1
    else:
        # 不用考虑相等的情况 题目中已经排除了这种可能性
        remaining_bucket_num += end_milk_in_order[end_milk_index][2]
        end_milk_index += 1
print(total_bucket_num)
