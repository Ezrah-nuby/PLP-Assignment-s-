my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

#inserting an element
my_list.insert(1, 15)
print(my_list)

#Extending with another List
another_list = [50, 60, 70]
my_list.extend(another_list)
print(my_list)

#removing Elements
del my_list[7]
print(my_list)

#ascending order
my_list.sort()
print(my_list)