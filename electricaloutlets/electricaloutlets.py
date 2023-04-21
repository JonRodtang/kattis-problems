num_lines = int(input())
powered = 0

for _ in range(num_lines):
    powered = 0
    test_case = list(map(int, input().split()))
    test_case.pop(0)
    for power_strip in test_case:
        powered += power_strip - 1
    print(powered + 1)
