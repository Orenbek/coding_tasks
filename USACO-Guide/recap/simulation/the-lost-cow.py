# coding=utf-8

import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

start, end = map(int, input().split())
cur_pos = start
next_move = 1
cur_len = 0
while True:
    '''
    移动一段距离
    如果终点在移动方向 则判断一下会不会到达，否则就不用判断了
    更新cur_len
    更新next_move
    '''
    if (end - start) * next_move > 0 and abs(next_move) >= abs(end - start):
        # 同方向且超出终点
        cur_len += abs(end - cur_pos)
        break
    else:
        cur_len += abs(next_move) + abs(cur_pos - start)
        cur_pos = start + next_move
    next_move *= -2
print(cur_len)
