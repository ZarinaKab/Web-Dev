def Xor(x: int, y: int) -> int:
    if x == y:
        return 0
    return 1

x, y = map(int, input().split())
print(Xor(x, y))