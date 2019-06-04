def process_request(self, active_floors):
    """
    process_request : method to select lift and process request
    """
    # unique set of active_floors
    active_floors = list(set(active_floors))
    active_floors.sort()
    self.active_floors = active_floors

    print("Matching Floor Request With Elevator!!")

    # process each floor, select lift which is closest
    print("Active Floors => ", active_floors)
    for queue_counter, floor in enumerate(active_floors):
        distance = []
        # find optimal lift for each floor
        for elevator  in self.elevators:
            # if its is not already selected
            if not elevator.is_selected:
                distance.append(abs(elevator.on_floor - floor))
            else:
                distance.append(999)

        queue_counter = queue_counter % len(self.request_queue)
        # find the selected lift
        selected_lift = distance.index(min(distance))
        elevator_selected = self.elevators[selected_lift]

        # assign service queue
        elevator_selected.service_list = [floor] + self.request_queue[queue_counter]

        # set direction
        elevator_selected.direction = 1 if elevator_selected.on_floor <= floor else -1

        # mark as selected
        elevator_selected.is_selected = True

        # print information on screen
        print("************************************************")
        print("Lift number ", elevator_selected.lift_number)
        print("On floor ", elevator_selected.on_floor)
        print("Service list ", elevator_selected.service_list)
        print("Direction ", elevator_selected.direction)


    # process request for each elevator
    for elevator in self.elevators:
        if elevator.is_selected:
            print("---------------------------------------------------------")
            print("\t\t\tLift - {}".format(elevator.lift_number))
            print("---------------------------------------------------------")
            elevator.process_request()
