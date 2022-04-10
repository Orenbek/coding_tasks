import sys

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

N = int(input())
shell_at_position = [0, 1, 2]
counter = [0, 0, 0]

for i in range(N):
    a, b, g = map(int, input().split())
    shell_at_position[a - 1], shell_at_position[b - 1] = shell_at_position[b - 1], shell_at_position[
        a - 1]  # Perform Bessie's swapping operation
    counter[shell_at_position[g - 1]] += 1

print(max(counter))
