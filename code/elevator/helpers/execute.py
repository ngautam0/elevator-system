def execute_request(self, list_of_request):
    # run untill list_of_request is not finished
    while True:
        # set is running true
        self.is_running = True

        # if currently on floor which is in requets list
        if self.on_floor in list_of_request:
            # remove the processed one from the list
            while list_of_request.count(self.on_floor) > 0:
                list_of_request.remove(self.on_floor)
            # stop the lift, as it has reached one of its destination
            self.is_running = False
            self.current_status()

            # open door
            # close door
            self.open_door()
            self.close_door()

        # if we have processed all list of request - break
        if len(list_of_request) == 0:
            break

        # display current status and move
        self.current_status()
        self.move_one_step()
