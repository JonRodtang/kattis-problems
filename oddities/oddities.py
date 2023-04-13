from sys import stdin as s

lines = int(s.readline())

for _ in range(lines):
    num = int(s.readline())
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

