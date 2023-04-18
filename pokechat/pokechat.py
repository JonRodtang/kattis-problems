import textwrap as t
encoding = list(input())
code = [int(codes.lstrip("0")) for codes in t.wrap(input(), 3)]
output = ""

for c in code:
    output += encoding[c - 1]

print(output)


