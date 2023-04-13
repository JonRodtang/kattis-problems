

n = 7
for i in range(int(input())):
    skru = input()
    if n < 10 and skru == "Skru op!":
        n += 1
    elif n > 0 and skru == "Skru ned!":
        n -= 1

print(n)

