R, C = map(int, input().split())
parking = [0] * 5
city_map = []
for _ in range(R):
    city_map.append(input())

for i in range(0, R-1):
    #city_map[i] city_map[i+1]
    for j in range(0, C-1):
        block = city_map[i][j] + city_map[i][j+1] + city_map[i+1][j] + city_map[i+1][j+1]
        if block.count('#') == 0:
            parking[block.count('X')] += 1
for p in parking:
    print(p)


