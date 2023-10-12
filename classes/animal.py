class Animal:

    def __init__(self, _type, _location, _age=10):
        self._type = _type
        self._location = _location
        self._age = _age

    def getInfo(self):
        return {
            "Тип": self._type,
            "Ареал обитания": self._location,
            "Возраст": self._age
        }

    def setLocation(self):
        location = input("введите среду обитания: ")
        self._location = location

    def run(self):
        return "бежим вперед"
