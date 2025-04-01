# string operation in python

name = "Mritunjay Singh"
#print(name[0])
#print(name[-1])

print(name[1:1])
print(name[0:7:2])
print(name[::2])

length = len(name)
print(length)

print(name.upper())
print(name.lower())
print(name.split(" "))

print(name.count('n'))
print(name.find('n'))

print(name.replace('Mritunjay', 'Mohan'))

print('Mritunjay' in name)
print (name.endswith('g'))
print(name.capitalize())

