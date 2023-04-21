import math
height, factor, velocity, wind_speed = map(int, input().split())
dist = 0

while height > 0:
    velocity += wind_speed
    velocity -= max(1, math.floor(abs(velocity/10)))
    if velocity >= factor:
        height += 1
    elif 0 < velocity < factor:
        height -= 1
        if height == 0:
            velocity = 0
    elif velocity <= 0:
        velocity = 0
        height = 0
    if wind_speed > 0:
        wind_speed -= 1
    dist += velocity
print(dist)
