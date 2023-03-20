import math
a = int(input())
b = int(input())

for i in range(math.ceil(math.sqrt(a)), int(math.sqrt(b) + 1)):
        print(i**2)