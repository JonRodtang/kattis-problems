num_lines = int(input())


for _ in range(num_lines):
    expWithoutAd, expWithAd, costAd = map(int, input().split())
    
    diff = expWithoutAd - (expWithAd - costAd)
    
    if diff < 0:
        print("advertise")
    elif diff > 0:
        print("do not advertise")
    elif diff == 0:
        print("does not matter")
