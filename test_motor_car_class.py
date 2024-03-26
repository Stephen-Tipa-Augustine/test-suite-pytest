from main import MotorCar


class TestMotorCar:
    motor = MotorCar('Motor Car', 220, 2023, 'silver')

    def test__str__method(self):
        assert "silver Motor Car 220 2023" == self.motor.__str__()

    def test__move__method(self, capsys):
        self.motor.move()
        captured = capsys.readouterr()

        assert f"{self.motor.car_name} is moving\n" == captured.out

    def test__turn__method(self, capsys):
        self.motor.turn('left')
        captured = capsys.readouterr()

        assert f"{self.motor.car_name} is turning to: left\n" == captured.out

    def test__stop__method(self, capsys):
        self.motor.stop()
        captured = capsys.readouterr()

        assert f"{self.motor.car_name} is stopping\n" == captured.out

    def test__park__method(self, capsys):
        self.motor.park()
        captured = capsys.readouterr()

        assert f"{self.motor.car_name} is parking\n" == captured.out
