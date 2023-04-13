from sys import stdin as s
while True:
    jack, jill = map(int, s.readline().split())
    
    if jack == 0 and jill == 0:
        break

    jack_cds = {int(s.readline()) for _ in range(jack)}
    jill_cds = {int(s.readline()) for _ in range(jill)}
    
    print(len(jack_cds.intersection(jill_cds)))




