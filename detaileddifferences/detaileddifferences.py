num_iterations = int(input())

for _ in range(num_iterations):
    line1 = input()
    line2 = input()
    diff = ""
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            diff += "."
        else:
            diff += "*"
    
    print(f"{line1}\n{line2}\n{diff}", end='\n\n')
