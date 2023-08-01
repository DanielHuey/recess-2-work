def dash():
    print("==========")


# ex1
"""
class Circle:
    def __init__(self, radius):
        pi = 3.141592653
        print("Area is:", pi*radius*radius, "squared units")
        print("Circumference is:", 2*pi*radius, "units")


c = Circle(5)
dash()
"""

# ex2
"""
class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def get_bonus(self):
        print("Bonus is: " + str(self.salary*0.15))


empl1 = Employee("E1", 150000)
empl1.get_bonus()
empl2 = Employee("E2", 230000)
empl2.get_bonus()
dash()
"""


# encapsulation
"""
class Encap:
    def __init__(self, account_number: int, balance: int):
        self.__acno = account_number
        self.__bal = balance

    def get_details(self):
        print("Account Number:", self.__acno)
        print("Balance:", self.__bal)

    def set_ac_no(self, newno: int):
        self.__acno = newno


e = Encap(23141, 1000)
e.get_details()
e.__acno = 3232
e.get_details()
e.set_ac_no(3232)
e.get_details()
"""

"""
class CelcToFahr:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_fahr(self):
        temp = self.__celsius * 9
        temp = temp/5
        print("Temperature in Fahrenheit is:", temp, "°F")
        return temp

    def get_celc(self):
        print("Temp is", self.__celsius, "°C")

    def set_celc(self, val):
        self.__celsius = val
        self.get_celc()


temp = CelcToFahr(37)
temp.__celsius = 50
temp.get_fahr()
temp.get_celc()
temp.set_celc(40)
"""
# Assignment1:  Show encapsulation with employee information to give a
# pay incrementation (Salary with employee information to new_salary)e.g from 850000 to 1000000


class Employee:
    def __init__(self, name: str, salary: int):
        self._name = name
        self._salary = salary

    def set_new_salary(self, new_salary: int):
        if self._salary > new_salary:  # only incrementation is allowed
            print("New salary MUST be greater than old salary.")
        else:
            print("Salary for", self._name, "has been increased from", self._salary,
                  "UGX to", new_salary, "UGX")
            self._salary = new_salary

    def get_salary(self):
        print("The salary for", self._name, "is", self._salary, "UGX")
        return (self._salary)


employee = Employee("Jeff", 850000)
employee.get_salary()
employee.set_new_salary(1000)
employee.set_new_salary(1000000)
