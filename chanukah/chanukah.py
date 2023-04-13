num_lines = int(input())

for _ in range(num_lines):
    index, holiday_days = map(int, input().split())
    print(index, sum([c for c in range(1, holiday_days + 1)]) + holiday_days)




