# coding=utf-8

def find_modifications(arr):
    # find total sum
    arr_sum = sum(arr)
    # try all resulting number of values
    # 1 2 3 1 1 1 -> 3 3 3 (3 resulting values)
    for i in range(len(arr), 0, -1):
        # must be a divisor of sum
        if arr_sum % i == 0:
            div = arr_sum / i
            possible = True
            cur_sum = 0
            for j in range(len(arr)):
                cur_sum += arr[j]
                if cur_sum > div:
                    possible = False
                    break
                elif cur_sum == div:
                    cur_sum = 0
            if possible:
                return len(arr) - i
    return -1


N = int(input())
for _ in range(N):
    input()
    arr = list(map(int, input().split()))
    print(find_modifications(arr))


