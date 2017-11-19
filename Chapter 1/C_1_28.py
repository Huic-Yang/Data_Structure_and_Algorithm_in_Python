from math import sqrt


def euclidean_norm(v):
  return sqrt(sum((x * x for x in v)))

vectors = [
  [1, 1, 1, 1],
  [1, 1, 1],
  [1, 1],
  [1]
]


if __name__ == "__main__":
  for v in vectors:
    print(euclidean_norm(v))
