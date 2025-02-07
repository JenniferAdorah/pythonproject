# using oop create a class called cars that have the
# following attributes model, colour and year of manufacture.
# Implement constructor method and add a method function that
# prints(my favourite car is that model, it is this in colour) and
# manufactured in ----years."Finally create five instance of that class"

class Cars:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year
    def myfunction(self):
        print(f"my favourite car is a{self.model}, it's color is{self.color} and it was made in {self.year} ")
myobject =Cars("Audi", "blue",  2024)
myobject.myfunction()
myobject1 =Cars("Tesla", "peach",  2023)
myobject1.myfunction()
myobject2 =Cars("Mercedes ", "black",  2022)
myobject2.myfunction()
myobject3=Cars("G wagon", "beige",  2021)
myobject3.myfunction()
myobject4=Cars("Mazda demio", "lavender",  2020)
myobject4.myfunction()
myobject5=Cars("Toyota", "violet",  2019)
myobject.myfunction()

