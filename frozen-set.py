frozen = frozenset() #empty frozen set
frozen2 = frozenset({1, 3, 5})
frozen3 = frozenset({"1", "2", "3"})
frozen4 = {frozenset({2, 5, 6}), frozenset({"2", "HI", "Jo"})}

print(frozen)
print(frozen2)
print(frozen3)
print(frozen4)

#set and frozenset
subset = set()


N = 4
for i in range(1, N + 1):
    for j in range(i+1, N+1):
        subset.add(frozenset({i,j}))

print(subset)

#create a set that has every subset of {1, 2, ...N}

N = 4

subsets = set()
subsets.add(frozenset())

for i in range(1, N + 1):

    new_subsets = set()
    for subset in subsets: #to check every subset
        nonfz = set(subset)
        nonfz.add(i)
        fz = frozenset(nonfz)
        new_subsets.add(fz)
    subsets.update(new_subsets)

print(subsets)
