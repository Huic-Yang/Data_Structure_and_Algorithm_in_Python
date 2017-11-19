def write_out_of_range(data):
  try:
    data[len(data)] = data[0]
  except IndexError:
    print("Don't try buffer overflow attacks in Python!")

if __name__ == "__main__":
  data = [1]
  write_out_of_range(data)
