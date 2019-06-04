import time
import random
import numpy as np

class Elevator:
    """
    Elevator class : represents a single elevator
    It can do following:
    1. Move up and down.
    2. Represented by lift_number
    3. Decides which direction to move based on service_list and on_floor
    4. on_floor property denotes currently is on floor.
    5. open and close door.
    6. Start moving and stop moving
    """
    def __init__(self, lift_number, floor_min, floor_max, on_floor = 0):
        self.lift_number = lift_number
        self.is_operational = True
        self.floor_max = floor_max
        self.floor_min = floor_min
        self.is_selected = False
        self.is_running = False
        self.on_floor = on_floor
        self.direction = 1
        self.is_overload = False
        self.service_list = []

    from elevator.helpers.move import move_one_step
    from elevator.helpers.execute import execute_request

    # prints the current status
    def current_status(self):
        print("lift {} is currently @ floor {}".format(self.lift_number, self.on_floor))
        print("lift {} running status {} ".format(self.lift_number, self.is_running))

    # open door
    def open_door(self):
        print("lift {} door opening".format(self.lift_number))
        self.door_open = True

    # close door
    def close_door(self):
        print("lift {} door closing".format(self.lift_number))
        self.door_open = False

    def calculate_service_in_directions(self):
        """
        Creates 2 list from a single service list
        service_in_up_direction - contains all the floor number which are above
        service_in_down_direction - all floor which are below
        """
        self.service_list = np.sort(self.service_list)
        service_in_up_direction = list(self.service_list[self.service_list > self.on_floor])
        service_in_down_direction = list(self.service_list[self.service_list < self.on_floor])
        service_in_down_direction = service_in_down_direction[::-1]
        return service_in_up_direction, service_in_down_direction

    def process_request(self):
        """
        recieves service_list and process them.
        Broabdly 2 tasks:

        TASK 1
        # case when button is pressed from outside
        # go to the requested floor

        TASK 2
        # process request when button from inside are pressed.
        """

        # go to requested floor
        print("Need To Process => ", self.service_list)
        if self.service_list[0] != self.on_floor:
            self.current_status()
            self.execute_request(self.service_list[0:1])
        else:
            self.current_status()
            self.open_door()
            self.close_door()

        # then user presses the buttons
        # lift decides automatically
        self.service_list = self.service_list[1:]
        service_in_up_direction, service_in_down_direction = self.calculate_service_in_directions()


        # nothing to service in up direction, go down
        if len(service_in_up_direction) == 0:
            self.direction = -1
        # nothing to service in down direction, go up
        elif len(service_in_down_direction) == 0:
            self.direction = 1
        # calculate cost and then decide direction
        # strategy could be improved
        # currently it just checks the first request for cost calculation
        else:
            # effort_up = distance between first up floor and current floor
            effort_up = abs(service_in_up_direction[0] - self.on_floor)
            # effort_down = distance between first down floor and current floor
            effort_down = abs(service_in_down_direction[0] - self.on_floor)

            # choose direction
            if effort_up <= effort_down:
                self.direction = 1
            else:
                self.direction = -1


        # execute once for up
        # once for down
        for turn in range(0,2):
            if self.direction == -1:
                self.execute_request(service_in_down_direction)

            else:
                self.execute_request(service_in_up_direction)

            # reverse the direction
            self.direction = - self.direction


        # set params to denote that it is available
        self.reset_lift_params()

    def reset_lift_params(self):
        # when request finishes reset the direction
        self.direction = 1
        self.is_running = False
        self.is_selected = False
        self.service_list = []
