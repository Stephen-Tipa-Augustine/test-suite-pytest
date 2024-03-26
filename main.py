from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self,  name, speed, model, color):
        self.car_name = name
        self.speed = speed  # kilometers per hour
        self.model = model
        self.color = color

    @abstractmethod
    def move(self):
        raise NotImplementedError

    @abstractmethod
    def turn(self, direction):
        raise NotImplementedError

    @abstractmethod
    def stop(self):
        raise NotImplementedError

    @abstractmethod
    def park(self):
        raise NotImplementedError

    def __str__(self):
        return f"{self.color} {self.car_name} {self.speed} {self.model}"


class MotorCar(Car):
    def __init__(self, name, speed, model, color):
        super().__init__(name, speed, model, color)

    def move(self):
        print(f"{self.car_name} is moving")

    def turn(self, direction):
        print(f"{self.car_name} is turning to: {direction}")

    def stop(self):
        print(f"{self.car_name} is stopping")

    def park(self):
        print(f'{self.car_name} is parking')


class Application:
    def __init__(self):
        self.car_collections = dict()
        self.car_collections['motor'] = MotorCar("Jeep", 220, 2023, 'silver')

    def start(self):
        for car in self.car_collections:
            print('--------------------------------')
            print(self.car_collections[car].__str__())
            print('********************************')


if __name__ == "__main__":
    app = Application()
    app.start()
