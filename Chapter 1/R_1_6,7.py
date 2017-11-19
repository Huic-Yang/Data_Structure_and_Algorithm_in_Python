def sum_odd_square_to(n):
  return sum((x*x for x in range(n) if x > 0 and x % 2 == 1))


if __name__ == "__main__":
  print(sum_odd_square_to(0))
  print(sum_odd_square_to (11))
  print(sum_odd_square_to(-11))
