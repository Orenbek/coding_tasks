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
    更新cur_len
        判断有没有到达重点
    更新next_move
    '''
    temp = cur_pos
    if next_move > 0:
        if end > cur_pos:
            cur_pos = end if cur_pos + next_move > end else cur_pos + next_move
        else:
            cur_pos = cur_pos + next_move
    else:
        if end < cur_pos:
            cur_pos = end if cur_pos + next_move < end else cur_pos + next_move
        else:
            cur_pos = cur_pos + next_move
    cur_len += abs(cur_pos - temp)
    next_move = next_move * -2
    if cur_pos == end:
        break
print(cur_len)
