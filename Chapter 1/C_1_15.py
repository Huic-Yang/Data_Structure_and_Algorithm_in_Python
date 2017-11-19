def is_unique(data):
  for i in range(len(data)):
    for j in range(len(data)):
      if i != j and data[i] == data[j]:
        return False
  return True


datas = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
  [1, 3, 5, 7, 9, 1],
  [1],
  []
]

if __name__ == "__main__":
  print([is_unique(data) for data in datas])
