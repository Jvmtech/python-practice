# find duplicate character in string

name = "Mritunjay Singh"

for i in name:
    if name.count(i) > 1:
        print("duplicate character is", i)