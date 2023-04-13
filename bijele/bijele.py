from sys import stdin as s


pieces = list(map(int, (s.readline().split())))
reference = [1, 1, 2, 2, 2, 8]
alterations_needed = []
for i, p in enumerate(pieces):
    alterations_needed.append(reference[i] - p) 

print(' '.join(map(str, alterations_needed)))
