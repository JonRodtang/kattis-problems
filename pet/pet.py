winner = 0
score = 0
for i in range(5):
    sum_points = sum(list(map(int, input().split())))
    
    if score < sum_points:
        winner = i+1
        score = sum_points
print(winner, score)
