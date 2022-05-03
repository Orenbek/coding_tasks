"""
ID: orenbek1
LANG: PYTHON3
TASK: gift1
"""
import sys

sys.stdin = open('gift1.in', 'r')
sys.stdout = open('gift1.out', 'w')
person_num = int(input())
persons = {input(): 0 for _ in range(person_num)}  # Dict Comprehensions. useful stuff
for _ in range(person_num):
    person_name = input()
    total_money, split_num = map(int, input().split())
    if split_num == 0:
        # notice split_num could be 0 and divide num can't be zero
        continue
    persons[person_name] = persons[person_name] - total_money + (total_money % split_num)
    for _ in range(split_num):
        persons[input()] += total_money // split_num
for key, value in persons.items():
    print(key, value)
