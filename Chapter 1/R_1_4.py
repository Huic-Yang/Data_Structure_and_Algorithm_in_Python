def sum_to(n):
  ans = 0
  i = 0
  while i < n:
    ans += i * i
    i += 1
  return ans


if __name__ == "__main__":
  print(sum_to(0))
  print(sum_to(11))
  print(sum_to(-11))
