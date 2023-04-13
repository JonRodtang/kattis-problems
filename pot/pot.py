from sys import stdin as s

x = 0
for _ in range(int(s.readline().rstrip())):
    n = int(s.readline().rstrip())
    m = n % 10
    n = n // 10
    x += n**m
print(x)
