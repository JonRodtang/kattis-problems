from sys import stdin as s

num_strings = int(s.readline())

strings = [s.readline().rstrip() for _ in range(num_strings)]
concats = [map(int, s.readline().split()) for _ in range(num_strings - 1)]

for a, b in concats:
    a = a - 1
    b = b - 1
    strings[a] = strings[a] + strings[b]
    strings[b] = ""


print(''.join(strings))




