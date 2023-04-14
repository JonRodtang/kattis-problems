string = list(input())

while string != []:
    if string[0] != 'a':
        string.pop(0)
    elif string[0] == 'a':
        print(''.join(string))
        break


