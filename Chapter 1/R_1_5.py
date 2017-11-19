def sum_to(n):
  return sum((x*x for x in range(n) if x > 0))


if __name__ == "__main__":
  print(sum_to(0))
  print(sum_to(11))
  print(sum_to(-11))
