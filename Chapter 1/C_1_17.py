def scale(data, factor):
  for val in data:
    val *= factor

data = [1, 2, 3, 4]
scale(data, 2)
print(data) # [1, 2, 3, 4]
