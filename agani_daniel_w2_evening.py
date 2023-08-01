"""def greet(name="Guest"):
    print(f"Hello {name:-^15}" + ", welcome to the lecture!")


greet()
greet(input("Enter your name, student: "))

tup1 = ('Banana', 'Matooke', 'Grapes', 'Dates', 'Apples', 'Oranges')
lis1 = list(tup1)
index = 0
for item in lis1:
    item = input(f'Enter new value for {item}: ')
    if item.strip() != "":
        lis1[index] = item
        # so you can just press enter to leave an item unedited
    index = index+1
print(lis1)
tup1 = tuple(lis1)
print(tup1)"""

# exceptions and files


class AganiException(Exception):
    def __init__(self, message):
        return super().__init__(message)


with open('agani.txt', 'w') as agani:
    loop = True
    while loop:
        try:
            no_of_lines = int(
                input('How many lines do you want in the text?: '))
            for x in range(no_of_lines):
                agani.write(input(f"[Line {x+1}]: ")+"\n")
            loop = False
            raise AganiException("")
        except ValueError:
            print("Please provide a valid number")
        except AganiException:
            print("Caught Custom Exception")
    print("Saved your info to 'agani.txt'")
