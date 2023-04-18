num_judges, already_rated = map(int, input().split())

sum_already_rated = 0
for _ in range(already_rated):
    sum_already_rated += int(input())


max_possible = (sum_already_rated + 3 * (num_judges - already_rated)) / num_judges
min_possible = (sum_already_rated - 3 * (num_judges - already_rated)) / num_judges
print(min_possible, max_possible)
