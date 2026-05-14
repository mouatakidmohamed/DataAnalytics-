class Restaurant:
    """This class stores information about a restaurant and prints basic restaurant messages."""

    def __init__(self, rest_name, food_type):
        # I store the restaurant name and food type as instance variables.
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")


restaurant_1 = Restaurant('Marrakech Grill', 'Moroccan food')
restaurant_2 = Restaurant('Pasta House', 'Italian food')
restaurant_3 = Restaurant('Taco Spot', 'Mexican food')

for restaurant in [restaurant_1, restaurant_2, restaurant_3]:
    restaurant.describe_rest()
    restaurant.rest_open()
