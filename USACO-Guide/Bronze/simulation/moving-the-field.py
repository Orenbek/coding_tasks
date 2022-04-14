# coding=utf-8
import sys

sys.stdin = open('mowing.in', 'r')
sys.sdtout = open('mowing.out', 'w')

N = int(input())
operations = [[val if i == 0 else int(val) for i, val in enumerate(input().split())] for _ in range(N)]
graph = [[0, 0]]
cur_x, cur_y = 0, 0
min_time = float('inf')
for direct, dist in operations:
    for i in range(dist):
        if direct == 'N': cur_y -= 1
        if direct == 'E': cur_x += 1
        if direct == 'S': cur_y += 1
        if direct == 'W': cur_x -= 1
        if [cur_x, cur_y] not in graph:
            graph.append([cur_x, cur_y])
        else:
            length = 0
            for x in range(len(graph) - 1, -1, -1):
                if graph[x] == [cur_x, cur_y]:
                    length = x
                    break
            min_time = min(min_time, len(graph) - length)
            graph.append([cur_x, cur_y])
print(-1 if min_time == float('inf') else min_time)
