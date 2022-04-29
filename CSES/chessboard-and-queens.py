chessboard = [list(input()) for _ in range(8)]
'''
dfs遍历+对路径进行记忆
'''
possible_count = 0


def check_available(i, j):
    if chessboard[i][j] == "*":
        return False
    for _i in range(0, i):
        if chessboard[_i][j] == "#":
            return False
        if j - _i - 1 >= 0 and chessboard[i - _i - 1][j - _i - 1] == "#":
            return False
        if j + _i + 1 < 8 and chessboard[i - _i - 1][j + _i + 1] == "#":
            return False
    return True


def recursive_search(level):
    global possible_count
    global chessboard
    if level == 8:
        possible_count += 1
        return
    for j in range(8):
        if check_available(level, j):
            chessboard[level][j] = "#"
            recursive_search(level + 1)
            chessboard[level][j] = "."


recursive_search(0)
print(possible_count)
