# itertools: product, permutations, combinations, accumulate, groupby, & infinite itertools

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, cycle, repeat

a = [1, 2, 3]
b = [4, 5, 6]
prod = product(a, b)
print(list(prod))

perm = permutations(a)
print(list(perm))

comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

acc = accumulate(a)
print(list(acc))

def smaller_than_3(x):
  return x < 3

persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Clarke', 'age': 20}]

group_obj = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj:
  print(key, list(value))
