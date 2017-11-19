def print_reverse():
  lst = []
  while True:
    try:
      lst.append(input())
    except EOFError:
      break
  while lst:
    print(lst.pop())

if __name__ == "__main__":
  print_reverse()
