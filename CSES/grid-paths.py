# coding=utf-8
grids = [[0 for _ in range(7)] for _ in range(7)]

given_path = list(input())
direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
# top right bottom left


def search_path(path_index, cor_x, cor_y):
    # 染色
    grids[cor_x][cor_y] = 1
    if cor_x == 6 and cor_y == 0 and path_index == len(given_path) - 1:
        # 走到头了 走出来了
        # 去色
        print("xxx")
        grids[cor_x][cor_y] = 0
        return 1
    # 规划下一步路径
    ret = 0
    if given_path[path_index] != "?":
        if given_path[path_index] == "U" and cor_x - 1 >= 0 and grids[cor_x - 1][cor_y] == 0:
            ret += search_path(path_index + 1, cor_x - 1, cor_y)
        elif given_path[path_index] == "R" and cor_y + 1 < 7 and grids[cor_x][cor_y + 1] == 0:
            ret += search_path(path_index + 1, cor_x, cor_y + 1)
        elif given_path[path_index] == "D" and cor_x + 1 < 7 and grids[cor_x + 1][cor_y] == 0:
            ret += search_path(path_index + 1, cor_x + 1, cor_y)
        elif given_path[path_index] == "L" and cor_y - 1 >= 0 and grids[cor_x][cor_y - 1] == 0:
            ret += search_path(path_index + 1, cor_x, cor_y - 1)
    else:
        for x, y in direction:
            if 0 <= cor_x + x < 7 and 0 <= cor_y + y < 7 and grids[cor_x + x][cor_y + y] == 0:
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



