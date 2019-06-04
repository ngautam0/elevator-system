from elevator_system.initialize import initialize_system
from elevator_system.main import ElevatorSystem

def run():
    """
    Run - It takes a total of 5 input.
    Make changes to this file to change the parameters.

    active_floors -  floors on which button has been pressed.
    lift_positions - current position of the lift
    no_of_lifts - total number of lifts
    floor_min - the lowest level floor number
    floor_max - the top level floor number
    request_each - request 2d array, represents request for each elevator

    # Assumption
    1. For simplicity i have assumed that there is just a single call button
    2. there is no up and down button on each floor
    3. each floor has a single button to call lift.
    4. each lift individually based on its service queue decides weather to go up or down
    """

    # floors on which the button has been pressed in this sequence
    active_floors = [5,-2,7,9,10, 9, 12, -1]

    # default position of lifts, as of now we have got 5 lifts in place
    lift_positions = [9,10,5,0,4]

    # no_of_lifts, floor_min, floor_max = initialize_system()
    no_of_lifts, floor_min, floor_max = 5, -4, 20

    # request for each elevator
    request_each = [[-3,12, 8, 6 ,4 ,0, 5],
                    [-3,0, 5],
                    [4,0, 5],
                    [8, 6 ,4 ,0, 5],
                    [2,4,8,10,12]]

    # create the elevator system
    elevator_system = ElevatorSystem(no_of_lifts, floor_min, floor_max, request_each, lift_positions)

    # process request
    elevator_system.process_request(active_floors)

if __name__ == '__main__':
    run()
