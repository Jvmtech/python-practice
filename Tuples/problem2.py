# 2. Given a list of tuples (name, score), sort it by score in descending order.

my_list = [("mohan", 90), ("sohan", 80), ("mohan", 70), ("sohan", 60), ("mohan", 50)]
my_list.sort(key=lambda x: x[1], reverse=False)
print(my_list)

