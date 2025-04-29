#__init__ behaviour:
class Electronic:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
 
electronic1 = Electronic("Laptop", "Dell", 1200, 5)
electronic2 = Electronic("Smartphone", "Samsung", 800, 10)
electronic3 = Electronic("Headphones", "Sony", 150, 20)
 
print(electronic1)
print(electronic2)
print(electronic3)
 
#__repr__ behaviour:
class Electronic:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
 
    def __repr__(self):
        return f"Electronic(name='{self.name}', brand='{self.brand}', price={self.price}, quantity={self.quantity})"
 
electronic1 = Electronic("Laptop", "Dell", 1200, 5)
print(electronic1)
 
#Data Encapsulation:
class Electronic:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.__price = price
        self.quantity = quantity
        self.__discount = None
 
    def set_discount(self, discount):
        self.__discount = discount
 
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
 
    def __repr__(self):
        return f"Electronic(name='{self.name}', brand='{self.brand}', price={self.get_price()}, quantity={self.quantity})"
 
# Instantiate an examples of Electronics
one_laptop = Electronic("Laptop", "Dell", 1200, 1)
 
multi_laptops = Electronic("Laptop", "Acer", 1500, 10)
multi_laptops.set_discount(0.20)
 
print(one_laptop.get_price())
print(multi_laptops.get_price())
print(one_laptop)
print(multi_laptops)
 
class Electronic:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.__price = price
        self.quantity = quantity
        self.__discount = None
 
    def set_discount(self, discount):
        self.__discount = discount
 
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
 
    def __repr__(self):
        return f"Electronic, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, quantity:{self.quantity}"
 
class Laptop(Electronic):
    def __init__(self, name, brand, price, quantity, processor):
        super().__init__(name, brand, price, quantity)
        self.processor = processor
 
class Phone(Electronic):
    def __init__(self, name, brand, price, quantity, display_size):
        super().__init__(name, brand, price, quantity)
        self.display_size = display_size
 
laptop1 = Laptop('XPS 15', 'Dell', 1800, 25, 'Intel Core i7')
laptop1.set_discount(0.15)
 
phone1 = Phone('Galaxy S20', 'Samsung', 800, 215, '6.2 inches')
phone1.set_discount(0.22)
 
print(laptop1)
print(phone1)
 
#Polymorphism:
class Electronic:
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.__price = price
        self.quantity = quantity
        self.__discount = None
 
    def set_discount(self, discount):
        self.__discount = discount
 
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
 
    def __repr__(self):
        return f"Electronic, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, quantity:{self.quantity}"
 
class Laptop(Electronic):
    def __init__(self, name, brand, price, quantity, processor):
        super().__init__(name, brand, price, quantity)
        self.processor = processor
 
class Phone(Electronic):
    def __init__(self, name, brand, price, quantity, display_size):
        super().__init__(name, brand, price, quantity)
        self.display_size = display_size
 
    def __repr__(self):
        return f"Phone, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, display_size:{self.display_size}"
 
# Instantiate a Phone object
phone1 = Phone("Smartphone", "Samsung", 1000, 2, 6.2)
 
# Instantiate a Laptop object
laptop1 = Laptop("Notebook", "HP", 800, 3, "Intel i5")
 
# Print the objects, invoking their respective __repr__ methods
print(phone1)
print(laptop1)    
 
#Abstraction:
from abc import ABC, abstractmethod
 
 
class Electronic(ABC):
    def __init__(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.__price = price
        self.quantity = quantity
        self.__discount = None
 
    def set_discount(self, discount):
        self.__discount = discount
 
    def get_price(self):
        if self.__discount:
            return self.__price * (1-self.__discount)
        return self.__price
 
    @abstractmethod
    def __repr__(self):
        return f"Electronic, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, quantity:{self.quantity}"
 
class Laptop(Electronic):
    def __init__(self, name, brand, price, quantity, processor):
        super().__init__(name, brand, price, quantity)
        self.processor = processor
 
class Laptop(Electronic):
    def __init__(self, name, brand, price, quantity, processor):
        super().__init__(name, brand, price, quantity)
        self.processor = processor
 
    def __repr__(self):
        return f"Laptop, name:'{self.name}', brand:'{self.brand}', price:{self.get_price()}, processor:{self.processor}"
# Instantiate a Laptop object
laptop1 = Laptop("Notebook", "HP", 800, 3, "Intel i5")
 
# Instantiate a Phone object
phone1 = Phone("Smartphone", "Samsung", 1000, 2, 6.2)
 
# Print the objects
print(phone1)
 
print(laptop1)
 
#Method Overloading:
class MathOperations:
    def add(self, a=0, b=0, c=0):
        return a + b + c
math_obj = MathOperations()
 
# Call the method with different argument counts
print(math_obj.add())      
print(math_obj.add(1))      
print(math_obj.add(1, 2))  
print(math_obj.add(1, 2, 3))
 
#using variable list argument:
class MathOperations:
    def add(self, *args):
        total = sum(args)
        return total
 
# Create an instance
math_obj = MathOperations()
 
# Call the method with different argument counts
print(math_obj.add())      
print(math_obj.add(1))      
print(math_obj.add(1, 2))  
print(math_obj.add(1, 2, 3))
 
#Method Overriding:
class Shape:
    def area(self):
        return 0
 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def area(self):
        return 3.14 * self.radius * self.radius
 
class Square(Shape):
    def __init__(self, side):
        self.side = side
 
    def area(self):
        return self.side * self.side
 
# Instantiate objects
circle = Circle(5)
square = Square(4)
 
# Call the overridden methods
print("Area of Circle:", circle.area())
print("Area of Square:", square.area())
 
# Call the base class method
shape = Shape()
print("Area of Shape:", shape.area())
 