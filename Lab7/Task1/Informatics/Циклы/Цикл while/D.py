N = int(input())

ok = False
i = 100
while i != -1:
    if N == pow(2, i):
        ok =True
    i -= 1

if ok:
    print("YES")
else:
    print("NO")