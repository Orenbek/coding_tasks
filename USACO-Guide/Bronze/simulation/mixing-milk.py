# coding=utf-8

from functools import reduce
import sys

sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

N = 3
capacity = [0 for i in range(N)]
milk = [0 for i in range(N)]
milk_map = {}
milk_record = []

"""
N is the number of buckets (which happens to be a constant value of 3)
capacity[i] is the maximum capacity of bucket i
milk[i] is the current amount of milk in bucket i
Taking into account the possible repetitions, use milk_map to record the results each time, until there are repetitions.
Afterwards, the result of each step needs to be recorded, so a number is needed to store it.
"""


def pour(i, j):
    amt = min(milk[i], capacity[j] - milk[j])
    # Amount of milk to pour is the minimum of the remaining milk in bucket i
    # and the available capacity in bucket j
    milk[i] -= amt
    milk[j] += amt


def main():
    for i in range(N):
        capacity[i], milk[i] = map(int, input().split())
    for i in range(100):
        pour(i % N, (i + 1) % N)  # Pour milk from one bucket to the next
        k = reduce(lambda a, b: str(a) + '_' + str(b), milk)
        if k in milk_map:
            index = milk_map[k]
            cycle_len = i - index
            for j in range(N):
                print(milk_record[index + (99 - i) % cycle_len][j])
                # 99 - i 表示剩下多少个数字 再取余 表示还需要往后读多少个数字
            return
        milk_map[reduce(lambda a, b: str(a) + '_' + str(b), milk)] = i
        milk_record.append(milk.copy())

    for i in range(N):
        print(milk[i])


main()
