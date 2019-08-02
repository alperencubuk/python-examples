# Comprehensions

list1 = [ item for item in range(10) if item%2==0 ]
print(list1)

list2 = [ item if item>5 else 0 for item in list1 ]
print(list2)

list3 = [ *[item for item in range(10)] ]
print(list3)

list4 = [ item for item in range(10) ]
print(list4)

data = {
    'name':'alp',
    'lastname': None,
    'age':0 }

data = { key:value for key,value in data.items() if value is not None }
print(data)

# Alperen Cubuk