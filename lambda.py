# Lambda Functions

from functools import reduce

l1 = lambda n: n*2
print(l1(3))

print((lambda n: n*2)(3))

l2 = lambda name,lastname: f'{name} - {lastname}'
data = {'name': 'alperen', 'lastname': 'cubuk'}
print(l2(**data))

l3 = lambda x: (str(x) if x > 0 else x)
print(l3(2))

number_list = range(-5,5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

items = [1,2,3,4,5]
squared = list(map(lambda x: x**2, items))
print(squared)

product = reduce((lambda x,y: x * y),[1,2,3,4])
print(product)

nt = lambda x: (lambda y: str(y))(x)*x
print(nt(3))

# Alperen Cubuk