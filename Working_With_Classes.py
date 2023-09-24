class Car():
    def __init__(self, model, color, inital_speed = 0):
        self.model = model
        self.color = color
        self.speed = inital_speed

    def speed_up(self):
        self.speed += 5
    
    def slow_down(self):
        self.speed -= 5

    def show_speed(self):
        print('Current speed: ', self.speed)


my_lovely_car = Car('Challenger', "black")
my_lovely_car.speed_up()
my_lovely_car.speed_up()
my_lovely_car.speed_up()
my_lovely_car.show_speed()





class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet = Dog('Brian', 3)
print(my_pet.__dict__)

my_pet.color = 'black'
print(my_pet.__dict__)

del my_pet.name
print(my_pet.__dict__)
