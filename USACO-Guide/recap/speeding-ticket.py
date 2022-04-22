# coding=utf-8
import sys

sys.stdin = open('speeding.in', 'r')
sys.stdout = open('speeding.out', 'w')

N, M = map(int, input().split())
road_sags = [list(map(int, input().split())) for _ in range(N)]
drive_sags = [list(map(int, input().split())) for _ in range(M)]
index1, index2 = 0,0
max_speed = 0
while index1 < N or index2 < M:
    max_speed = max(max_speed, drive_sags[min(index2, M - 1)][1] - road_sags[min(index1, N - 1)][1])
    # 注意这里index1和index2都可能会超出index限制 因此做个比较聪明的处理
    if index2 == M or road_sags[index1][0] < drive_sags[index2][0]:
        # 这里的处理也需要注意index有没有可能超出限制或者是road_sags[index1][0] 和 drive_sags[index2][0]相等的情况
        index1 += 1
    else:
        index2 += 1
print(max_speed)
