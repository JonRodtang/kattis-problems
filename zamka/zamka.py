# N(xxxx) = X = M(xxxx)
# L <= M,N <= D minimize N maximize
L = int(input())
D = int(input())
X = int(input())

N = L
M = D

for _ in range(D-L):
    if sum([int(d) for d in str(N)]) == X:
        break
    else:
        N += 1

for _ in range(D-L):
    if sum([int(d) for d in str(M)]) == X:
        break
    else:
        M -= 1
print(N)
print(M)
