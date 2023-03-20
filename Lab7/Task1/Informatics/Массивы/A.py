n = int(input())
mass = list(map(int, input().split()))

for i in range(n):
    if i % 2 == 0:
        print(mass[i], end = ' ')