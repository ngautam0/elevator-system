from elevator.main import Elevator

class ElevatorSystem:
    """
    ElevatorSystem - Class that contains array of Elevator objects
    self.number_of_lifts = total number of lifts in the system
    self.floor_max = top floor
    self.floor_min = bottom most floor
    self.request_queue = request queue for each lift

    """

    def __init__(self, number_of_lifts, floor_min, floor_max,request_each, lift_positions=[]):
        self.number_of_lifts = number_of_lifts
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.elevators = []
        self.request_queue = request_each

        # safegaurd in case no initial positining of lift is given
        # all start from 0 in that case.
        if len(lift_positions) < 0:
            lift_positions = [0] * number_of_lifts

        # create an array of elevator objects
        for each in range(0, number_of_lifts):
            new_elevator = Elevator(each, floor_min, floor_max,lift_positions[each])
            self.elevators.append(new_elevator)


    from elevator_system.helpers.process import process_request
