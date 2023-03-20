def in1to10(n, outsideMode):
  if outsideMode:
    return (n <= 1 or n >= 10)
  else:
    return (n >= 1 and n <= 10)