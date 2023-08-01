"""
multiline comments
"""


def dash():
    print("==========")

# def main(text="Guest"):
#     print("Hello " + text)


# if __name__ == "__main__":
#     name = "Daniel"
#     main(name)

"""
list []
tuples ()

dict {}, separate with commas
e.g {name: "Agani", age: 5} or {ace,bee,cat}

set {} e.g {ace,bee,cat}
"""

# cars = {'Tesla', 'Bugatti', 'Pagani', 'McLaren', 'Toyota'}
# for car in cars:
#     print(car)
"""
# dictionary
dict = {'phone': 'blackberry',
        'color': 'black',
        'model': 'BDD100-1',
        'model_name': 'Blackberry Motion'}

# dictionary values()
print(dict.values())

# checking for key existence


def does_key_exist(key: str):
    for k in dict.keys():
        if k == key:
            print('Key "'+key+'" exists!')
            return
    print('Key "'+key+'" does not exist!')


does_key_exist('color')
does_key_exist('meat')

# editing dictionary items
dict['color'] = 'Blue'
print(dict)

# adding to & removing from dictionary
dict['brand'] = 'Ford'
print(dict)
dict.pop('brand')
print(dict)

# looping through a dictionary
for k, v in dict.items():
    print(k, v)
"""

# Day 3
"""
a = 10
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a % b)
print(a**b)
dash()

# Comparison
print('Is a > b ?', a > b)
print('Is a >= b ?', a >= b)
print('Is a < b ?', a < b)
print('Is a <= b ?', a <= b)
print('Is a == b ?', a == b)
print('Is a != b ?', a != b)
dash()

# logical
c = True
d = False

print('c and d:', c and d)
print('c or d:', c or d)
print('not c:', not c)
print('not d:', not d)
dash()

# assignment operators
e = 11
print(e)
e += 5  # 16
print(e)
e -= 2  # 14
print(e)
e *= 2  # 28
print(e)
e /= 4  # 7.0
print(e)
e %= 4  # 3.0
print(e)
e **= 3  # 27.0
print(e)
dash()

# membership addignment operators (in)
cars = {'Mazda', 'Maserati', 'Rolls Royce',
        'Pagani', 'Chevrolet', 'Volkswagen'}
print('Toyota' in cars)
print('Mazda' in cars)
dash()

# identity operators (is)
f = 4
g = 4
print(f is g)
print(f is not g)

dash()

# bitwise operators
"" "
Bitwise And = &
Bitwise Or = |
Bitwise Xor = ^
Bitwise Not = ~
Bitwise Left shift = <<
Bitwise Right shift = >>
"" "
a = 2
print(a)
print(~a)
print('{:b}'.format(~a))
dash()
"""
