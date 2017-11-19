from itertools import permutations


lst = ['c', 'a', 't', 'd', 'o', 'g']
for s in permutations(lst):
  print(''.join(s))
