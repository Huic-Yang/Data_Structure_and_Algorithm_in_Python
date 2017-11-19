from random import randrange

def my_choice(data):
  return data[randrange(len(data))]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

if __name__ == "__main__":
  print(my_choice(data))
  print(my_choice(data))
  print(my_choice(data))
