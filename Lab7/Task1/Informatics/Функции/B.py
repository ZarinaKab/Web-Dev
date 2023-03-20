def power(a: float, n: int) -> float:
    return a ** n

a, n = map(float, input().split())
print(power(a, int(n)))