######################### Example without __init__ method ###############################

class Car:  
    # Without __init__, directly defining attributes afterward  
    def start_engine(self):  
        status = "Engine started."  # Local variable  
        print(status)
        
# Creating an instance of Car  
my_car = Car()  

# Setting attributes directly after the instance is created  
my_car.make = "Maruti"  
my_car.model = "Dzire"  
my_car.year = 2021

print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")  
my_car.start_engine()

####################### Example with __init__ method ######################################

class Car:  
    def __init__(self, make, model, year):  
        self.make = make    # Instance attribute
        self.model = model  # Instance attribute
        self.year = year    # Instance attribute
        
    def start_engine(self):  
        status = "Engine started."  # Local variable  
        print(status)
        
# Creating an instance of Car with attributes defined in __init__  
my_car = Car(make="Maruti", model="Dzire", year=2021)  

print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")  
my_car.start_engine()

###################### Example of self in a Class ##############################
class Car:  
    def __init__(self, make, model, year):  
        self.make = make        # Instance attribute  
        self.model = model      # Instance attribute  
        self.year = year        # Instance attribute  

    def start_engine(self):  
        status = "Engine started."  # Local variable  
        print(status)  

    def display_info(self):  
        # Use self to access instance attributes  
        print(f"My car is a {self.year} {self.make} {self.model}.")  

# Creating an instance of Car  
my_car = Car(make="Maruti", model="Dzire", year=2021)   

# Calling methods  
my_car.start_engine()      # Calling an instance method  
my_car.display_info()      # Displaying the car info

####################### ID of Instance and ID of self ############################
class MyClass:
    def __init__(self, value):
        self.value = value

    def display_id(self):
        print(f"ID of self: {id(self)}")


# Create an instance of MyClass
class_instance = MyClass(10)
print(f"ID of instance: {id(class_instance)}")

# Calling the method to check IDs
class_instance.display_id()

####################### Creating an instance and calling the methods ###########################
class Car:  
    def __init__(self, make, model, year):  
        self.make = make         # Instance attribute  
        self.model = model       # Instance attribute  
        self.year = year         # Instance attribute  
    
    def start_engine(self):  
        status = "Engine started."  # Local variable  
        print(status)               # Prints the engine status  

    def display_info(self):  
        # Print car information using instance attributes  
        print(f"My car is a {self.year} {self.make} {self.model}.")  


# Creating an instance of Car  
my_car = Car(make="Maruti", model="Dzire", year=2021)  

# Calling methods  
my_car.start_engine()       
my_car.display_info()     

###################### Class and Instance Variables ################################

class Car:  
    # Class variable to track the number of cars created  
    number_of_cars = 0  

    def __init__(self, make, model, year):  
        self.make = make          # Instance variable  
        self.model = model        # Instance variable  
        self.year = year          # Instance variable  

        # Increment the class variable whenever a new instance is created  
        Car.number_of_cars += 1  

    def display_info(self):  
        """Display the information of the car."""  
        print(f"{self.year} {self.make} {self.model}")  

    @classmethod  
    def get_number_of_cars(cls):  
        """Class method to return the number of car instances created."""  
        return cls.number_of_cars  

# Creating instances of Car  
car1 = Car("Maruti", "Dzire", 2021)  
car2 = Car("Mahindra", "Scorpio", 2022)  
car3 = Car("Honda", "City", 2023)  

# Displaying information about individual cars  
car1.display_info()    
car2.display_info() 

# Accessing the class variable to get the number of cars created  
print(f"Total cars created: {Car.get_number_of_cars()}")  

############################## Creating a Class #######################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
person1 = Person("Anmol", 22)
print(person1.name)