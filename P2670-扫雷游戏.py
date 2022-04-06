rowsNum = list(map(int, input().split()))[0]

coord = ({"x": -1, "y": -1}, {"x": -1, "y": 0}, {"x": -1, "y": 1}, {"x": 0, "y": -1},
         {"x": 0, "y": 0}, {"x": 0, "y": 1}, {"x": 1, "y": -1}, {"x": 1, "y": 0}, {"x": 1, "y": 1})

gameMatrix = [list(input()) for i in range(rowsNum)]

colsNum = len(gameMatrix[0])
for i in range(rowsNum):
    for j in range(colsNum):
        if gameMatrix[i][j] != "*":
            cnt = 0
            for item in coord:
                corX = i + item["x"]
                corY = j + item["y"]
                if corX < rowsNum and corX >= 0 and corY < colsNum and corY >= 0 and gameMatrix[corX][corY] == "*":
                    cnt += 1
            print(cnt, end='')
        else:
            print("*", end='')
    print()
