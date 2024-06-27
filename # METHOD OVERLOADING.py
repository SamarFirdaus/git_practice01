import pdb
# METHOD OVERLOADING
# 1 - Default parameter values
class Calculator:
    def add(self, a, b = 0):
        return a + b


cal1 = Calculator() 
print(cal1.add(1, 5))


# using variable length or variable length keyword:

class Calculator1:
    def add(self, *args):
        if len(args) == 1:
            pdb.set_trace()
            return args[0]
        elif len(args) == 2:
            return sum(args)
        elif len(args) >= 2:
            return sum(args)
        else:
            return None
        

cal2 = Calculator1()

result = cal2.add(2, 3, 4)
print(result)

# iheritance


class Shape:
    def __init__(self, name):
        self.name = name
    
    def area(self):
        raise


NotImplementedError("subcalss must must implement this method")


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height    

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius, pie=3.14):
        super().__init__(name)
        self.radius = radius
        self.pie = pie

    def area(self):
        return self.pie*self.radius**2


circle1 = Circle("cirle", 2)
print(circle1.area())         

rect1 = Rectangle("rectangle", 5, 3)
print(rect1.area())


class Vehicle:
    def move(slef):
        print("Vehcle is moving")


class Radio:
    def radio(self):
        print("Radio plays Music")



class Car(Vehicle, Radio):
    def honk(self):
        print("Car honks")


car = Car()
car.move()

car.radio()

car.honk()

#method overriding


class Animal:
    def speak(Self):
        print("Animal speaks")


class Dog:
    def speak(self):
        print("Dog barks")


animal = Animal()
animal.speak()

dog = Dog()
dog.speak()


class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Name:{self.name}, Employee ID : {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department    

    def display_info(self):
        super().display_info()
        print(f"Depatment: {self.department}")



class Developer(Employee):
    def __init__(self, name, emp_id, language):
        super().__init__(name, emp_id)
        self.language = language

    def display_info(self):
        super().display_info()
        print(f"Language : {self.language}")


manager = Manager("Muzaffar", 1,"HR")
manager.display_info()    

dev = Developer("Zubiya", 1, "PHP")
dev.display_info()

