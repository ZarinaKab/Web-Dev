 

import math

 

def CountDivisors(n):

  res = 1

  for i in range(2, int(math.sqrt(n)) + 1):

    if (n % i == 0):

      c = 0

      while (n % i == 0):

        n //= i

        c += 1

      res *= (c + 1)

  if (n > 1): res *= 2

  return res

 

n = int(input())

print(CountDivisors(n))