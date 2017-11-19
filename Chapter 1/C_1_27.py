def factors(n): # generator that computes factors
  k = 1
  lst = []
  while k * k < n: # while k < sqrt(n)
    if n % k == 0:
      yield k
      lst.append(n // k)
    k += 1
  if k * k == n: # special case if n is perfect square
    yield k
  while lst:
    yield lst.pop()


if __name__ == "__main__":
  for i in factors(100):
    print(i, end=' ')
  print()
