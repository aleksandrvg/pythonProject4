from classes.animal import Animal
from classes.test import Car

wolf = Animal("волк", "лес")
pig = Animal("свинья", "город", 4)
animals = [wolf, pig]
for ani in animals:
    print(ani.getInfo())
    # ani.setLocation()

car = Car()
car.setMotor(wolf)
print(car.forward())
