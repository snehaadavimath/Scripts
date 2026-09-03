
# List are mutable
# ordered collection of different datatype
# cretaed by using []
# since list are mutable we can operate CRUD operte99999mm/

vegies = ['carrot', 'beans', 'onion']

# print(vegies)

# print(vegies[0])

vegies.insert(0,'tomato')
print(vegies)

# print(vegies)

vegies.append('brinjal')
print(vegies)

# print(vegies)

vegies.extend(['drumstick','potato', 'chillies'])
print(vegies)

# print(vegies)

vegies.remove('potato')
print(vegies)

vegies.pop()
print(vegies)

print(len(vegies))

# to convert list into String
print(''.join(vegies))
