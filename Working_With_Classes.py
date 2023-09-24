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
