from functools import reduce

add10 = lambda x: x + 10
print(add10(5))

a = [1, 2, 3, 5, 6, 8]
product_a = reduce(lambda x, y: x*y, a)
print(product_a)
