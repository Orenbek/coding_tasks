# coding=utf-8
import sys

sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')

N, M = map(int, input().split())
road_sags = [list(map(int, input().split())) for _ in range(N)]
drive_sags = [list(map(int, input().split())) for _ in range(M)]
for i in range(len(road_sags)):
    if i == 0:
        road_sags[i].append(road_sags[i][0])
    else:
        road_sags[i].append(road_sags[i][0] + road_sags[i - 1][2])
for i in range(len(drive_sags)):
    if i == 0:
        drive_sags[i].append(drive_sags[i][0])
    else:
        drive_sags[i].append(drive_sags[i][0] + drive_sags[i - 1][2])
'''
为了计算方便 每段路程最后添加了一个元素为累计路程长度
'''
index1, index2 = 0, 0
max_speed = 0
while index1 < N or index2 < M:
    max_speed = max(max_speed, drive_sags[min(index2, M - 1)][1] - road_sags[min(index1, N - 1)][1])
    # 注意这里index1和index2都可能会超出index限制 因此做个比较聪明的处理
    if road_sags[index1][2] < drive_sags[index2][2]:
        index1 += 1
    elif road_sags[index1][2] > drive_sags[index2][2]:
        index2 += 1
    else:
        # 不用考虑index会超出的情况了 因为这一步同时保证了到达最后一节时 两者都会新增1
        index1 += 1
        index2 += 1
print(max_speed)
