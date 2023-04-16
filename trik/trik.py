cups = [1, 0, 0]
moves = list(input())

for m in moves:
    if m == 'A':
        cups[0], cups[1] = cups[1], cups[0]
    elif m == 'B':
        cups[1], cups[2] = cups[2], cups[1]
    elif m == 'C':
        cups[0], cups[2] = cups[2], cups[0]

for i, c in enumerate(cups):
    if c != 0:
        print(i + 1)
        break



