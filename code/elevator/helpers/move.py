import time

def move_one_step(self):
    """
    move_one_step : moves lift one step up or down based on direction
    self.on_floor = self.on_floor + self.direction
    direction can have value of 1 or -1
    raises Exception if lift is not operational
    """
    try:
        if self.is_operational:
            self.on_floor = self.on_floor + self.direction
        else:
            raise Exception("Lift is not operational")

    except Exception as e:
        print(e)
        return e
