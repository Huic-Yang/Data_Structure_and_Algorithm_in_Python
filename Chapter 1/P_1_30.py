def div_times(n):
  times = 0
  while 2 <= n:
    times += 1
    n /= 2
  return times


if __name__ == "__main__":
  print(div_times(100))
  print(div_times(-100))
  print(div_times(2))
