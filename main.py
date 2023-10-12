from classes.animal import Animal
from classes.test import Car
from classes.test2 import Animall
from classes.test3 import Car2
from random import randint

wolf = Animal("волк", "лес")
pig = Animal("свинья", "город", 4)

animals = [wolf, pig]
for ani in animals:
    print(ani.getInfo())
    # ani.setLocation()

car = Car()
car.setMotor(wolf)
print(car.forward())

# animal1 = Animall("Заяц", randint(100, 200))
# animal2 = Animall("Волк", randint(100, 200))
# animal3 = Animall("Утка", randint(100, 200))
# animalls = [animal1, animal2, animal3]

animalls = []
animalName = ['Заяц', 'Черепаха', 'Утка', 'Гусь', 'Собака']
for name in animalName:
    animalls.append(Animall(name, randint(100, 200)))

road = int(input("введите длину дороги: "))
for anima in animalls:
    if anima.getSpeed() >= road:
        print(f"{anima.getType()} пробежал")
    else:
        print(f"{anima.getType()} сошел с дистанции")

car01 = Car2('Модель-1', '100лс', 'Синий')
car02 = Car2('Модель-2', '200лс', "Красный")
car03 = Car2('Модель-3', '300лс', 'Зеленый')
car04 = Car2('Модель-4', '400лс', 'Белый')
car05 = Car2('Модель-5', '500лс', 'Черный')
carModel = [car01, car02, car03, car04, car05]

for model in carModel:
    print(model.getBody(), model.getMotor(), model.getColor())
