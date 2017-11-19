def dot_product(a, b):
  if len(a) != len(b) or len(a) == 0:
    return None
  return [a[i] * b[i] for i in range(len(a))]


array_pairs = [
  ([1, 2, 3], [3, 2, 1]),
  ([1, 1, 1], [2, 2, 2]),
  ([1, 2], [2, 1]),
  ([], []),
  ([], [1])
]

if __name__ == "__main__":
  for x, y in array_pairs:
    print(dot_product(x, y))
