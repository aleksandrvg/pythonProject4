from classes.animal import Animal


class Car:
    motor: Animal

    def setMotor(self, motor: Animal):
        self.motor = motor

    def forward(self):
        return self.motor.run()
