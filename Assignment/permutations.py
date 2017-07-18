import itertools
perm = [1,2,3]
print("\nPrinting all the permutations of [1,2,3]: ")
a = set(itertools.permutations(perm))
print(list(a))