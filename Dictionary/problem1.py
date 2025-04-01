# Given dictionary
a ={
    "key":"value",
    "harry":"code",
    "marks":"100",
    "list":[1,2,9]
}

# print key
print(a["key"])

# print disctionary into list of tuple
print(a.items())

# print dictionary keys list
print(a.keys())

# adding new key with value in dictionary
a.update({"test":"checking"})
print(a)

# removing key from dictionary
a.pop("marks")
print(a)

# clear dictionary
a.clear()
print(a)

# delete dictionary
del a
print(a)




