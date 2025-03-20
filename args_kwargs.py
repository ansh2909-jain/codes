def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling functions
print_args(5, 6, 7, "Hello")
print_kwargs(Name="Anmol", Age=23, Job="Engineer")

###############################################################################

def print_info(name, *args, **kwargs):
    print(f"Name: {name}")
    print("Other Info:", args)
    print("Additional Details:", kwargs)

print_info("Anmol", 23, "Engineer", Location="New Delhi", Hobby="Reading")