GCVWR, truck_weight, num_items = map(int, input().split())
items_weights_total = sum(list(map(int, input().split())))
GCVWR_90_without_truck = (GCVWR - truck_weight) * 0.9

print(int(GCVWR_90_without_truck - items_weights_total))



