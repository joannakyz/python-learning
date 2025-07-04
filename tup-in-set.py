N = 5 
A = set()
AA = set()
for i in range(1, N + 1):
    A.add(i)

print("A: ", A)

for j in A:
    tup = (j, j**2)
    AA.add(tup)
    
print("AA: ", AA)
