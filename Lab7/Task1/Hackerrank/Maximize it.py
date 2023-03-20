from itertools import product

k, m = map(int, input().split())

# Read in the input sets
sets = []
for i in range(k):
    sets.append(list(map(int, input().split()))[1:])

# Compute the maximum value of the expression using itertools.product
max_val = 0
for combination in product(*sets):
    val = sum([x**2 for x in combination]) % m
    if val > max_val:
        max_val = val

print(max_val)
