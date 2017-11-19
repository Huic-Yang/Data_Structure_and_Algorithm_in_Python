def count_volwels(s):
  cnt = 0
  vowels = ('a', 'e', 'i', 'o', 'u')
  for ch in s:
    if ch in vowels:
      cnt += 1
  return cnt

strings = [
  "Hello", "Python", "Data", "Structure"
]


if __name__ == "__main__":
  print([count_volwels(s) for s in strings])
