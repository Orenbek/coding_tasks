"""
ID: orenbek1
LANG: PYTHON3
TASK: beads
"""
import sys

sys.stdin = open('beads.in', 'r')
sys.stdout = open('beads.out', 'w')
N = int(input())
beads = list(input())
max_len = 0
for i in range(N):
    right_char = None
    right_len = 0
    while right_len < N:
        char = beads[(i + right_len) % N]
        if right_char is not None and char != "w" and right_char != char:
            break
        if right_char is None and char != "w":
            right_char = char
        right_len += 1
    left_char = None
    left_len = 0
    while left_len < N:
        char = beads[i - 1 - left_len]
        if left_char is not None and char != "w" and left_char != char:
            break
        if left_char is None and char != "w":
            left_char = char
        left_len += 1
    if right_len + left_len > max_len:
        max_len = right_len + left_len
print(min(max_len, N))
# 40min
