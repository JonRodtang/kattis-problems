text = input()

for index, char in enumerate(text):
    if (char == char.upper()) and (char != chr(45)):
        print(char, end='')
print("")
