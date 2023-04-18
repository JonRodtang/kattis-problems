width = int(input())
num_pieces = int(input())

area = 0

for _ in range(num_pieces):
    x, y = map(int, input().split())
    area += x * y


length = area / width

print(int(length))

