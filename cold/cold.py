num_temps = input()
line2 = input()

temps = line2.split(' ')


neg_temps = 0

for i in range(int(num_temps)):
    if int(temps[i]) < 0:
        neg_temps += 1
print(neg_temps)








