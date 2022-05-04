# coding=utf-8
import sys

sys.stdin = open('blist.in', 'r')
sys.stdout = open('blist.out', 'w')

cows = [list(map(int, input().split())) for _ in range(int(input()))]  # [start, end, bucket_num][]
start_milk_in_order = sorted(cows, key=lambda x: x[0])  # cows.sort是原地排序 sorted是返回新的数组
end_milk_in_order = sorted(cows, key=lambda x: x[1])

start_milk_index = 0
end_milk_index = 0
total_bucket_num = 0
remaining_bucket_num = 0
while start_milk_index < len(cows) or end_milk_index < len(cows):
    # 这里的判断和speeding ticket那里的判断基本一致
    if end_milk_index == len(cows) or (start_milk_index < len(cows) and start_milk_in_order[start_milk_index][0] < end_milk_in_order[end_milk_index][1]):
        if start_milk_in_order[start_milk_index][2] > remaining_bucket_num:
            total_bucket_num += start_milk_in_order[start_milk_index][2] - remaining_bucket_num
            remaining_bucket_num = 0
        else:
            remaining_bucket_num -= start_milk_in_order[start_milk_index][2]
        start_milk_index += 1
    else:
        remaining_bucket_num += end_milk_in_order[end_milk_index][2]
        end_milk_index += 1
print(total_bucket_num)
