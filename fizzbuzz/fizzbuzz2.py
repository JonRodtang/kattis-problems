from sys import stdin as s


first_div, second_div, lines = map(int, s.readline().split())

for i in range(lines):
    output = ""
    if ((i+1) % first_div == 0):
        output += "Fizz"
    if ((i+1) % second_div == 0):
        output += "Buzz"
    
    if output:
        print(output)
    else:
        print(i+1)
