# coding=utf-8

[nth, order_num] = list(map(int, input().split()))
matrix = [[i + (j * nth) + 1 for i in range(nth)] for j in range(nth)]


def rotate(x, y, r, clock_wise):
    # x和y表示第几行 从0开始
    temp = [[0 for _i in range(r * 2 + 1)] for _j in range(r * 2 + 1)]
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            '''
            matrix: [0 , 1]
                    [-1, 0]
            变换之后的坐标为 matrix·[x] = (y,-x)
                                 [y]
            上述的变换是按原点在(0,0)处的旋转得到的公式，但我们矩阵是按照(r,r)点去旋转的，因此还得有个位移
            将旋转中心移动至(r,r)
            先旋转或者是先矩阵变换都是可以的，不相互影响。因为移动不会对矩阵进行相乘操作，不会存在先后问题。
            因此上面的公式坐标还得向上和想右分别移动r，于是得到最终结果是 f(x,y) = (y+r, -x+r)
            '''
            # matrix[x+i][y+j]表示matrix[x][y]点附近的所有点的集合
            if clock_wise:
                temp[j + r][-i + r] = matrix[x + i][y + j]
            else:
                temp[-j + r][i + r] = matrix[x + i][y + j]
    for i in range(-r + x, r + x + 1):
        for j in range(-r + y, r + y + 1):
            matrix[i][j] = temp[i - x + r][j - y + r]


for index in range(order_num):
    [x, y, r, z] = list(map(int, input().split()))
    rotate(x - 1, y - 1, r, True if z == 0 else False)
print(matrix)
