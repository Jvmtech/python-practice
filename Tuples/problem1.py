# tupes in pythons

tup = (1,2,3,4,5)
print(tup)

print(tup[-1])

print(tup[1:4])

print(tup[::-2])

print("length of tuple",len(tup))

print("max of tuple",max(tup))

print("min of tuple",min(tup))

print("sum of tuple",sum(tup))

print("sorted tuple",sorted(tup))

print("reversed tuple",tuple(reversed(tup)))

print("count of 3 in tuple",tup.count(3))

print("index of 3 in tuple",tup.index(3))

print("tuple to list",list(tup))

print("list to tuple",tuple([1,2,3,4]))

print("tuple to string",str(tup))

print("string to tuple",tuple("hello"))

print("tuple to set",set(tup))

print("set to tuple",tuple({1,2,3,4}))

print("tuple to dict",dict(tup))

print("dict to tuple",tuple({"a":1,"b":2,"c":3}))

print("tuple to frozenset",frozenset(tup))

print("frozenset to tuple",tuple(frozenset({1,2,3,4})))

print("tuple to bytes",bytes(tup))

print("bytes to tuple",tuple(b'hello'))

print("tuple to bytearray",bytearray(tup))

print("bytearray to tuple",tuple(bytearray(b'hello')))

print("tuple to memoryview",memoryview(tup))

print("memoryview to tuple",tuple(memoryview(b'hello')))