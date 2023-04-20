num_lines = int(input())

for _ in range(num_lines):
    beats, seconds = map(float, input().split())

    BPM      = round(60 * beats / seconds, 4)
    ABPM_min = round(60 / (seconds / (beats - 1)), 4)
    ABPM_max = round(60 / (seconds / (beats + 1)), 4)

    print(ABPM_min, BPM, ABPM_max)
