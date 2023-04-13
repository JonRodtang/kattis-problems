from sys import stdin as s

string = s.readline()

for i in range(len(string)):
    if string[i] != '\n':
        if string[i] == string[i+1] == 's':
            print("hiss")
            break
    else:
        print("no hiss")
