# coding=utf-8

import sys

# sys.stdin = open("lostcow.in", "r")
# sys.stdout = open("lostcow.out", "w")

cur_pos, end = map(int, input().split())
next_move = 1
cur_len = 0
while True:
    '''
    移动一段距离
    如果终点在移动方向 则判断一下会不会到达，否则就不用判断了
    更新cur_len
    更新next_move
    '''
    if (end - cur_pos) * next_move > 0 and abs(next_move) >= abs(end - cur_pos):
        # 同方向
        cur_len += abs(end - cur_pos)
        break
    else:
        cur_len += abs(next_move)
        cur_pos += next_move
    next_move *= -2
print(cur_len)
