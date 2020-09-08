
input_list = [5, 6, 2, 10, 35, 70, 5, 2, 1, 7]

def div_by_five(num):
  if num % 5 == 0:
    return True
  else:
    return False

xyz = (i for i in input_list if div_by_five(i)) # ---> this is a generator
# xyz = []
# for i in input_list:
#   if div_by_five(i):
#     xyz.append(i)

# for i in xyz:
#   print(i)

# [print(i) for i in xyz]

x = (((i, j) for j in range(5)) for i in range(5))

for i in x:
  for j in i:
    print(j)
