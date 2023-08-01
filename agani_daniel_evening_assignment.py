# friday assignment
# (my device got an issue so i failed to join in that lecture)
# lists
names = ["George", "Kim", "Phelis", "Cynthia", "Keith"]
print(names[1])
names.append('Arthur')
names.insert(2, 'Bathel')
print(names)
names.pop(3)  # or del names[3]
print(names)
print(names[-1])

numbers = [1, 2, 5, 6, 8, 9, 3]
print(numbers[2:5])

countries = ['Ghana', 'Ukraine', 'Imaginesia']
coun1 = countries.copy()
for c in coun1:
    print(c)

animals = ["lion", "elephant", "giraffe", "zebra", "cheetah"]
animals.sort()
print(animals)
animals.reverse()
print(animals)
for animal in animals:
    if 'a' in animal:
        print(animal)

l1 = ['Agani']
l2 = ['Daniel']
l3: list = list(zip(l1, l2))
print(l3)
print("---------------")

# tuples
x = ("samsung", "iphone", "tecno", "redmi")
print(x[0])
print(x[-2])
y = list(x)
y[1] = "itel"
x = tuple(y)
x = x + ("Huawei",)
print(x)
for v in x:
    print(v)
y = list(x)
y.pop(0)
x = tuple(y)
cities = tuple(["Kampala", "Arua", "Masaka", "Fort-Portal", "Mubende"])
for city in cities:
    print(city)
print(cities[1:4])
t1 = ("Agani",)
t2 = ("Daniel",)
t3 = t1+t2
tcol = ("Red", "Orange")
tcol = tcol * 3
print(tcol)
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
no_of_8 = 0
for num in thistuple:
    if num == 8:
        no_of_8 = no_of_8 + 1
print("8 appears", no_of_8, "times")
print("---------------")

# sets
bev = set(["Water", "Soda", "Juice"])
bev.add("milk")
bev.add("bushera")
print(bev)
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Present")
seta = {1, 2, 3, 4}
lista = [5, 6]
seta.update(lista)
print(seta)
set1 = {"21"}
set2 = {"Agani"}
set1.update(set2)
print(set1)
print("---------------")

# strings
int1 = 145
str1 = " Years"
join = ''.join([str(int1), str1])
print(join)
txt = ' Hello, Uganda! '
txt = txt.strip()
print(txt)
print(txt.upper())
txt = txt.replace("U", "V")
print(txt)
print(txt[1:4])
y = "I am proudly Ugandan"
x = 'All "Data Scientists" are cool!'
print("---------------")

# dictionaries
shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(shoes['size'])
shoes['brand'] = 'Adidas'
shoes.update([tuple(['type', 'sneakers'])])
print(shoes)
print(shoes.keys())
print(shoes.values())
if 'size' in shoes.keys():
    print("size exists")
for k, v in shoes.items():
    print(k, ":", v)
shoes.pop('color')
print(shoes)
skeys = shoes.copy().keys()
for k in skeys:
    shoes.pop(k)
aguy = {
    "name": "Nick",
    "color": "black",
    "age": 40
}
aguy2 = aguy.copy()
print(aguy2)

furniture = {
    'type': 'chair',
    'color_options': {
        'plastics': 'black',
        'wooden': 'brown'
    }
}
print(furniture)
print("---------------")
