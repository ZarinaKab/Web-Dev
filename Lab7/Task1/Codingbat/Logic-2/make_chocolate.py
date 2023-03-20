def make_chocolate(small, big, goal):
  # Calculate the maximum number of big bars we can use
  max_big_bars = goal // 5
  if big > max_big_bars:
    big = max_big_bars
  
  # Calculate the remaining weight we need to make up using small bars
  remaining_weight = goal - big*5
  
  # Check if we have enough small bars to make up the remaining weight
  if small >= remaining_weight:
    return remaining_weight
  else:
    return -1