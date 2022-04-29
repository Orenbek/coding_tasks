n = int(input())
arr = list(map(int, input().split()))


def search(i, s1, s2):
    if i == n:
        return abs(s2 - s1)
    return min(search(i + 1, s1 + arr[i], s2), search(i + 1, s1, s2 + arr[1]))


print(search(0, 0, 0))
