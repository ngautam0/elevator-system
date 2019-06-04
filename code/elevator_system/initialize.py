def initialize_system():
    """as of now this module is not being used..."""
    """need to incorporate more error handling before we can use this"""
    try:
        print("Initialize the Elevator System")
        no_of_lifts = int(input("Enter Number Of Elevator => "))
        floor_min = int(input("Enter The Minimum Floor => "))
        floor_max = int(input("Enter The Maximum Floor => "))

        if no_of_lifts <= 0:
            raise ValueError

        if floor_min > floor_max:
            raise ValueError

    except ValueError as e:
        print("ValueError Raised Due To Invalid Input")
        return e

    except Exception as e:
        print(e)
        return e

    else:
        return no_of_lifts, floor_min, floor_max
