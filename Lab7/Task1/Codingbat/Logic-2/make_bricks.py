def make_bricks(small, big, goal):
  if goal % 5 > small:
    return False
  if big * 5 + small < goal:
    return False
  return True