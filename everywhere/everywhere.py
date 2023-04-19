num_blocks = int(input())

for _ in range(num_blocks):
    num_lines = int(input())
    cities = []
    for _ in range(num_lines):
        cities.append(input())
    print(len(set(cities)))
