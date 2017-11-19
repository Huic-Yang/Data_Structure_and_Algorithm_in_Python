def minmax(data):
  try:
    mi = ma = data[0]
    for e in data:
      if e < mi:
        mi = e
      if ma < e:
        ma = e
    return mi, ma
  except IndexError:
    print("should not be an empty sequence!")
    return None, None
  except TypeError:
    print("elements in data must be comparable with each other")
    return None, None


datas = [
  [1, 2, 3, 4, 5],
  [1.1, 2.2, 3.3, 4.4, 5.5],
  ["a", "b", "c", "d", "e"],
  [1, "a", 2, "b", 3],
  []
]

if __name__ == "__main__":
  for data in datas:
    print(minmax(data))
