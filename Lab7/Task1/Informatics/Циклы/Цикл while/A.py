n = int(input())

i = 1
while i != n + 2:
# for i in range(1, n + 1):
    if i**2 <= n:
        print(i**2)
    i += 1