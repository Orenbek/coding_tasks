# coding=utf-8
import os
import time

grids = [[0 for _ in range(7)] for _ in range(7)]

given_path = list(input())
direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
# top right bottom left
'''
第一个版本由于层数太多 直接严重超时了 需要做optimization
观察发现一个特别重要的数学规律：
前进中碰到障碍物无法向前进了，那么观察一下左右两边是不是还有没有经过的方块，如果有则空方块就会被分成两块，其中有一块将永远都无法到达。
（因为我们刚开始就是从地图的边缘触发的，再次碰到障碍物必定会把整个grid一分为二）
根据上面的规律 再次分析发现可以分两种情况讨论：
情况1：障碍物就在前进方向上，相当于正面碰上  这种情况下只要查看一下当前方块位置的左右是不是都为空 如果为空 则肯定有一块访问不到了
情况2：我们和障碍物擦边遇上，障碍物出现在左边或者右边，这种情况下 我们也可以回退一步查看前一个方框的左右是不是都为空 如果为空 则肯定有一块访问不到了
'''


def is_empty(cor_x, cor_y):
    return 0 <= cor_x < 7 and 0 <= cor_y < 7 and grids[cor_x][cor_y] == 0


def is_obstacle(cor_x, cor_y):
    # 是墙或者是走过的方块
    return cor_x < 0 or cor_x >= 7 or cor_y < 0 or cor_y >= 7 or grids[cor_x][cor_y] == 1


def is_occupied(cor_x, cor_y):
    return 0 <= cor_x < 7 and 0 <= cor_y < 7 and grids[cor_x][cor_y] == 1


def approachable(cor_x, cor_y, dir_x, dir_y):
    x = cor_x + dir_x
    y = cor_y + dir_y
    if is_obstacle(x, y):
        return False
    # 查看正前方会不会遇到障碍
    if is_obstacle(cor_x + dir_x + dir_x, cor_y + dir_y + dir_y):
        # 看左右 是不是都是空方块
        if dir_x != 0:
            # 这一步是判断当前行进方向
            if is_empty(x, y + 1) and is_empty(x, y - 1):
                return False
        else:
            if is_empty(x + 1, y) and is_empty(x - 1, y):
                return False
    # 查看有没有擦边
    if dir_x != 0:
        if is_occupied(cor_x, cor_y + 1) or is_occupied(cor_x, cor_y - 1):
            # 擦边了
            if is_empty(cor_x, cor_y + 1) and is_empty(cor_x, cor_y - 1):
                return False
    else:
        if is_occupied(cor_x + 1, cor_y) or is_occupied(cor_x - 1, cor_y):
            # 擦边了
            if is_empty(cor_x + 1, cor_y) and is_empty(cor_x - 1, cor_y):
                return False
    return True


def print_grids():
    for i in range(7):
        for j in range(7):
            print(grids[i][j], " ", end="")
        print()


def search_path(path_index, cor_x, cor_y):
    # print_grids()
    # time.sleep(0.1)
    # os.system("clear")

    # 染色
    grids[cor_x][cor_y] = 1
    if cor_x == 6 and cor_y == 0:
        if path_index == len(given_path) - 1:
            # 走到头了 走出来了
            # 去色
            grids[cor_x][cor_y] = 0
            return 1
        else:
            grids[cor_x][cor_y] = 0
            return 0
    # 规划下一步路径
    ret = 0
    if given_path[path_index] != "?":
        if given_path[path_index] == "U" and approachable(cor_x, cor_y, -1, 0):
            # print("↑")
            ret += search_path(path_index + 1, cor_x - 1, cor_y)
        elif given_path[path_index] == "R" and approachable(cor_x, cor_y, 0, 1):
            # print("→")
            ret += search_path(path_index + 1, cor_x, cor_y + 1)
        elif given_path[path_index] == "D" and approachable(cor_x, cor_y, 1, 0):
            # print("↓")
            ret += search_path(path_index + 1, cor_x + 1, cor_y)
        elif given_path[path_index] == "L" and approachable(cor_x, cor_y, 0, -1):
            # print("←")
            ret += search_path(path_index + 1, cor_x, cor_y - 1)
    else:
        for x, y in direction:
            if approachable(cor_x, cor_y, x, y):
                # if x == -1 and y == 0:
                #     print("↑")
                # if x == 0 and y == 1:
                #     print("→")
                # if x == 1 and y == 0:
                #     print("↓")
                # if x == 0 and y == -1:
                #     print("←")
                ret += search_path(path_index + 1, cor_x + x, cor_y + y)
    # 去色
    grids[cor_x][cor_y] = 0
    return ret


grids[0][0] = 1
result = 0
if given_path[0] == "?":
    # 刚开始只能向右或者向下走
    result += search_path(0, 0, 1)
    result += search_path(0, 1, 0)
if given_path[0] == "R":
    result += search_path(0, 0, 1)
if given_path[0] == "D":
    result += search_path(0, 1, 0)
print(result)
