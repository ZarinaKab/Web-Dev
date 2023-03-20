def _min(a, b, c, d):
    return min(min(a, b), min(c, d))

arr = list(map(int, input().split()))
print(_min(arr[0], arr[1], arr[2], arr[3]))