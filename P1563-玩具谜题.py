m, n = map(int, input().split())  # m个玩具，n个指令
toys = []  # 所有玩具信息
for i in range(m):
    [dirr, name] = input().split()
    toys.append({"head": int(dirr), "name": name})

now = 0  # 当前位置
for i in range(n):
    [dirr, steps] = list(map(int, input().split()))
    if (toys[now]["head"] == 0 and dirr == 0) or (toys[now]["head"] == 1 and dirr == 1):
        now = (now + m - steps) % m
    elif (toys[now]["head"] == 0 and dirr == 1) or (toys[now]["head"] == 1 and dirr == 0):
        now = (now + steps) % m
print(toys[now]["name"])
