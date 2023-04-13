from sys import stdin as s

for line in s:
        a, b = map(int, line.split())
        print(abs(a - b))





