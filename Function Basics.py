# ACloudGuru Lab/Practice | "Function Basics"

def print_name(name):
    print(f"Name is {name}")

print_name("Brian")

# ---------------------------------------------------------------------------------- Separation

def add_two(num):
    return num + 2

result = add_two(2)
print(result)

print(add_two(4))

# ---------------------------------------------------------------------------------- Separation

def add(num1, num2):
    return num1 + num2

print(add(1, 5))

# ---------------------------------------------------------------------------------- Separation

def contact_card(name, age, car_model):
    return print(f"{name} is {age} and drives a {car_model}")

print(contact_card('Brian', 29, "Dodge Durango"))

# ---------------------------------------------------------------------------------- Separation

def can_drive(age, driving_age=16):
    return age >= driving_age

print(can_drive(29))

# ---------------------------------------------------------------------------------- Separation


