die1, die2 = map(int, input().split())
total = die1 + die2
outcomes = []
distribution = []

for i in range(1,die1+1):
    for j in range(1,die2+1):
        outcomes.append(i + j)

for i in range(2, total+1):
    distribution.append(outcomes.count(i))

# Two die rolls are normaly distributed 
mean = total // 2 - 1
outcomes = list(set(sorted(outcomes)))
num_most_common_elements = distribution.count(distribution[mean])
most_common_outcomes = [x for _, x in sorted(zip(distribution, outcomes))][-num_most_common_elements:]

for o in most_common_outcomes:
    print(o)
