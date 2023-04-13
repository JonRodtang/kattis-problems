from sys import stdin as s


num_lines = int(s.readline())

qaly = 0.0
for _ in range(num_lines):
    quality_life, period_year = map(float, s.readline().split())

    qaly += quality_life * period_year

print(f"{qaly:.3f}")
