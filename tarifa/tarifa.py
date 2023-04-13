from sys import stdin as s

megabytes = int(s.readline())
months = int(s.readline())
total_available = 0
for _ in range(months):
    total_available += megabytes - int(s.readline())

total_available += megabytes
print(total_available)
