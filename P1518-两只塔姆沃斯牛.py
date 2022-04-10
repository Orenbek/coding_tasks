# coding=utf-8

fields = [['*' for i in range(12)]]
for i in range(10):
    fields.append(['*', *list(input()), '*'])
fields.append(['*' for i in range(12)])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
positionFarmer, positionCow = (), ()
for i in range(1, 12):
    for j in range(1, 12):
        if fields[i][j] == 'F':
            positionFarmer = (i, j)
        if fields[i][j] == 'C':
            positionCow = (i, j)
        if positionCow and positionFarmer:
            break

time = 0
directFarmer = 0  # 初识方向向上
directCow = 0
while True:
    if time >= 100000:
        print(0)
        break
    if positionCow == positionFarmer:
        print(time)
        break
    cowXaxis = positionCow[0] + directions[directCow][0]
    cowYaxis = positionCow[1] + directions[directCow][1]
    if fields[cowXaxis][cowYaxis] == '*':
        directCow = (directCow + 1) % 4
    else:
        positionCow = (cowXaxis, cowYaxis)

    farmerXaxis = positionFarmer[0] + directions[directFarmer][0]
    farmerYaxis = positionFarmer[1] + directions[directFarmer][1]
    if fields[farmerXaxis][farmerYaxis] == '*':
        directFarmer = (directFarmer + 1) % 4
    else:
        positionFarmer = (farmerXaxis, farmerYaxis)
    time += 1
