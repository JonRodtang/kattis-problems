num_lines = int(input())
display_time = 0

if num_lines % 2 == 0:
    times_pressed = []
    for i in range(num_lines):
        times_pressed.append(int(input()))

    for i in range(0, num_lines + 1, 2):
        if i != num_lines:
            display_time += times_pressed[i + 1] - times_pressed[i]
    
    print(display_time)

else:
    print("still running")
