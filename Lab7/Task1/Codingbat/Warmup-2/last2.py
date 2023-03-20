def last2(str):
  if len(str) < 2:
    return 0
  last2 = str[-2:]
  count = 0
  for i in range(len(str) - 2):
    if str[i:i+2] == last2:
      count += 1
  return count
