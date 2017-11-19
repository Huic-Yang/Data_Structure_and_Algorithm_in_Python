def cal(x, y):
  yield x + y, '+'
  yield x - y, '-'
  yield x * y, '*'
  if y != 0:
    yield x / y, '/'


def func(a, b, c):
  for ans, sign in cal(a, b):
    if ans == c:
      print("{0} {1} {2} = {3}".format(a, sign, b, c))
  for ans, sign in cal(b, c):
    if ans == a:
      print("{0} = {1} {2} {3}".format(a, b, sign, c))


if __name__ == "__main__":
  while True:
    x = int(input())
    y = int(input())
    z = int(input())
    if x == y == z == 0:
      break
    func(x, y, z)
