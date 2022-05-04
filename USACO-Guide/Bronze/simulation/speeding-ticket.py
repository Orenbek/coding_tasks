# coding=utf-8
import sys

sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

n, m = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
journey = [list(map(int, input().split())) for _ in range(m)]

for i in range(len(road)):
    if i == 0:
        road[i].append(road[i][0])
    else:
        road[i].append(road[i][0] + road[i - 1][2])
for i in range(len(journey)):
    if i == 0:
        journey[i].append(journey[i][0])
    else:
        journey[i].append(journey[i][0] + journey[i - 1][2])
'''
为了计算方便 每段路程最后添加了一个元素为累计路程长度
'''
max_over_limit = 0
nth_sag_of_road = 0
nth_sag_of_trip = 0
'''
例子：
3 3
40 75
50 35
10 45
40 76
20 30
40 40
思路 通过两个变量记录当前走到的路段下标 比较当前节点累计走过的路程大小
当前节点 road和journey的路程均相等（例如刚开始时 都均为40公里），此时 nth_sag_of_road 和 nth_sag_of_trip 均向前一步
此时更小的路段应该是journey的路段，向前走了20公里，累计60公里，而road会走出90公里。
因此哪个更小就移动哪个下标。并且更新 max_over_limit 直至两个路程都迭代完
'''
while True:
    if nth_sag_of_road == len(road) - 1 and nth_sag_of_trip == len(journey) - 1:
        print(max_over_limit)
        break
    length, speed, journey_total_length = journey[nth_sag_of_trip]
    # 也可以写成 [length, speed, total_length] python很智能
    road_len, speed_limit, road_total_length = road[nth_sag_of_road]
    if speed > speed_limit and speed - speed_limit > max_over_limit:
        max_over_limit = speed - speed_limit
    if road_total_length < journey_total_length:
        nth_sag_of_road += 1
    elif road_total_length > journey_total_length:
        nth_sag_of_trip += 1
    else:
        nth_sag_of_road += 1
        nth_sag_of_trip += 1
        # 两者正好相等 需要同时走入下一个路段
