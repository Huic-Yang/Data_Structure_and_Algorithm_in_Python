from random import randint


def my_shuffle(data):
  for i in range(0, len(data)):
    j = randint(0, len(data) - 1)
    data[j], data[i] = data[i], data[j]


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_shuffle(data)
print(data)
