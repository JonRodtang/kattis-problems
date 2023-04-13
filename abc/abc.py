from sys import stdin as s


# a < b < c
nums = list(map(int, s.readline().split()))
chars = [*s.readline().rstrip()]
nums.sort()
final = []
for i, c in enumerate(chars):
    if c == 'A':
        final.append(nums[0])
    elif c == 'B':
        final.append(nums[1])
    elif c == 'C':
        final.append(nums[2])

print(' '.join(map(str, final)))
