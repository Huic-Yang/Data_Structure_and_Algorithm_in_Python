def remove_pounctuation(s):
  pounctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
  return ''.join(ch for ch in s if ch not in pounctuation)

strings = [
  "John's", "we'll", "they're", "he's", "I'am",
  "Thanks!", "What?", "(hehe)", "2^3", "@someone",
  "#include", "{}", "$200", "&var", "(@_@)"
]


if __name__ == "__main__":
  print([remove_pounctuation(s) for s in strings])
