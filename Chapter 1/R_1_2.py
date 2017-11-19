def is_even(k):
  if not isinstance(k, int):
    return False
  step = 2 if k >= 0 else -2
  sign = 1 if k >= 0 else -1
  while sign * k >= 0:
    if k == 0:
      return True
    k -= step
  return False


if __name__ == '__main__':
  print(is_even(0))
  print(is_even(10))
  print(is_even(11))
  print(is_even(-10))
  print(is_even(-11))
  print(is_even(1.1))
