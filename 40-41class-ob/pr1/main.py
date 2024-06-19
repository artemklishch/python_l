class Car:
    def move(self):
        print("Car is move")

    def stop(self):
        print("Car stopped")


my_car = Car()
my_car1 = Car()
print(type(my_car))
print(isinstance(my_car, Car))
my_car.move()
my_car.stop()

my_car1.stop()
print(my_car.__dict__)
print(my_car == my_car1)  # False
print({} == {})  # True

Car.move(my_car)  # Car is move
