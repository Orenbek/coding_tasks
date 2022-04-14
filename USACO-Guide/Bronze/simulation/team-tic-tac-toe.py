# coding-utf-8

import sys

sys.stdin = open('tttt.in', 'r')
sys.stdout = open('tttt.out', 'w')

board = [list(input()) for _ in range(3)]
# 本题可以轻松的进行枚举出来
single_vic = []
two_char_vic = []
for i in range(3):
    if len(set(board[i])) == 1:
        single_vic.append(board[i][0])
    elif len(set(board[i])) == 2:
        two_char_vic.append(','.join(set(board[i])))
        # set 会对内容进行排列 例如 set(['b', 'c', 'a']) 结果为 {'a', 'b', 'c'}
        # 因此可以直接join 然后再次做个set
    if len({board[0][i], board[1][i], board[2][i]}) == 1:
        single_vic.append(board[0][i])
    elif len({board[0][i], board[1][i], board[2][i]}) == 2:
        two_char_vic.append(','.join({board[0][i], board[1][i], board[2][i]}))

if len({board[0][0], board[1][1], board[2][2]}) == 1:
    single_vic.append(board[0][0])
elif len({board[0][0], board[1][1], board[2][2]}) == 2:
    two_char_vic.append(','.join({board[0][0], board[1][1], board[2][2]}))
if len({board[0][2], board[1][1], board[2][0]}) == 1:
    single_vic.append(board[0][2])
elif len({board[0][2], board[1][1], board[2][0]}) == 2:
    two_char_vic.append(','.join({board[0][2], board[1][1], board[2][0]}))

print(len(set(single_vic)))
print(len(set(two_char_vic)))
