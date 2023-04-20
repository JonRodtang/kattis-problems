cost_of_seed = float(input())
num_lawns = int(input())

area_to_sow = 0

for _ in range(num_lawns):
    width, length = map(float, input().split())
    area_to_sow += width * length

print(cost_of_seed * area_to_sow)
