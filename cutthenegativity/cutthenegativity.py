num_lines = int(input())

flights = []
for _ in range(num_lines):
    flights.append(list(map(int, input().split())))

num_direct_flights = len([flight for line in flights for flight in line if flight > 0])

print(num_direct_flights)



for i, line in enumerate(flights):
    for j, f in enumerate(line):
        if f > 0:
            print(i+1, j+1, f)



