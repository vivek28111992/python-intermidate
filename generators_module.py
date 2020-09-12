import sys

def firstn_generators(n):
  num = 0
  while num < n:
    yield num
    num += 1

print(sum(firstn_generators(10)))
print(sys.getsizeof(firstn_generators(1000000)))


def fibo(n):
  a, b = 0, 1
  while a < n:
    yield a
    a, b = b, a + b

f = fibo(10)
for i in f:
  print(i)
