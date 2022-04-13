# coding=utf-8

import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")


def main():
    start, end = map(int, input().split())
    if start == end:
        print(0)
        return
    cur = start
    total_length = 0
    times = 1
    # 当前行进的距离还不够，并且 start < cur <= end or end <= cur < start 或者是 cur和 end 在 start 的两边
    # 因此 cur - start 和 end - start 同号即可保证在一边
    while (abs(cur - start) < abs(end - start) and (cur - start) * (end - start) >= 0) or (cur - start) * (
            end - start) <= 0:
        cur = start + (2 * (times % 2) - 1) * 2 ** (times - 1)
        # 2 * (times % 2) - 1 为取正负号
        if times == 1:
            length = 1
        else:
            length = 3 * 2 ** (times - 2)
        # length表示每一回走过的路程
        total_length += length
        times += 1
    print(total_length - abs(cur - end))
    '''
    整体用时1h 花费时间太长的原因在于
    1.没有想清楚while循环的条件
    2.计算total_length的方式也没有想清楚
    3.计算当前每一回走过的路程公式也不对
    '''

main()
