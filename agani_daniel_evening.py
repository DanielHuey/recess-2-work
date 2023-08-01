def dash():
    print("==========")


# tup1 = (1, "hi", 2.33)
# print(len(tup1))
# dash()

# set1 = {1, 2, 3}
# print("The length of the set is "+str(len(set1))+" elements.")
# print("The data type of the set is "+str(type(set1))+".")
# dash()

# # Accessing items
# # items in set
# for i in set1:
#     print(i)
# dash()

# add to set
# print(set1)
# set1.add(99)
# print(set1)
# dash()

# combining
# set2 = {4, 6, 8}
# set1.update(set2)
"""
update or union can be used to combine 2 sets
the main difference is that update stores the value in the set 
that called the function, while union returns a set containing
the combination of the two sets
so union is used like; 
  new_set = set1.union(set2)
"""
# print(set1)

a = input('Give me a long word...\n')
print("It's length is", str(len(a)))  # len function
dash()
print(a[1:int(len(a)/2)+1])  # slicing
for i in a:  # for loop
    print(i)
dash()
