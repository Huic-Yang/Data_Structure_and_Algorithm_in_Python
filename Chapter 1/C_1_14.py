from random import randrange

def check(data):
  """ if there is a distinct pair of numbers in the sequence whose
      product is odd, return true. Otherwise return false."""
  for i in range(len(data)):
    for j in range(len(data)):
      if i != j and (data[i] * data[j]) % 2 == 1:
        return True
  return False


datas = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 0],
  [1, 3, 5, 7, 9],
  [2, 4, 6, 8, 0]
]

if __name__ == "__main__":
  print([check(data) for data in datas])
