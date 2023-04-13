from sys import stdin as s


first_div, second_div, lines = map(int, s.readline().split())

for i in range(lines):
    if ((i+1) % first_div == 0) and ((i+1) % second_div == 0):
        print("FizzBuzz")
    elif ((i+1) % first_div == 0):
        print("Fizz")
    elif ((i+1) % second_div == 0):
        print("Buzz")
    else:
        print(i+1)
