class Restaurant:
    """This class stores information about a restaurant."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")


class FoodTruck(Restaurant):
    """This child class adds food truck specific information."""

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)
        self.private_bookings = 'N'
        self.truck_location = ''
        self.location_history = []

    def accepts_private_bookings(self, answer):
        self.private_bookings = answer.upper()
        if self.private_bookings == 'Y':
            print('This food truck currently accepts private bookings.')
        else:
            print('This food truck currently does not accept private bookings.')

    def relocate_truck(self, location):
        self.truck_location = location
        self.location_history.append(location)
        print(f"Truck is currently located at {self.truck_location}")


truck = FoodTruck('Rolling Tacos', 'tacos')
truck.describe_rest()
truck.accepts_private_bookings('Y')
truck.relocate_truck('123 Main St, Washington DC')
truck.relocate_truck('456 Park Ave, Baltimore MD')
print(truck.location_history)
# I kept duplicate locations because a food truck may visit the same location on different days.
