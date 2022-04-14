import sys

sys.stdin = open('diamond.in', 'r')
sys.stdout = open('diamond.out', 'w')

N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
nums.sort()
max_len = 0
index = 0
for i in range(len(nums)):
    while nums[i] - nums[index] > K:
        index += 1
    max_len = max(max_len, i - index + 1)
print(max_len)
