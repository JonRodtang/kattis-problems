hours, minutes = map(int, input().split())

change = -45

minutes = minutes + change

if minutes < 0:
    hours -= 1
    minutes += 60
    if hours < 0:
        hours = hours + 24



print(hours, minutes)
