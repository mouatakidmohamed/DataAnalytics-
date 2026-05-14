class Restaurant:
    """This enhanced class tracks restaurant information, customers served, and ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self, customers_served):
        # I add today's customers to the running total.
        self.number_served += customers_served

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self, rating):
        # I only accept whole number ratings from 1 to 5.
        if isinstance(rating, int) and 1 <= rating <= 5:
            self.customer_ratings.append(rating)
            avg_rating = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {avg_rating:.2f}")
        else:
            print("Please reenter your rating as an integer from 1 to 5.")


restaurant_1 = Restaurant('Marrakech Grill', 'Moroccan food')
restaurant_2 = Restaurant('Pasta House', 'Italian food')
restaurant_3 = Restaurant('Taco Spot', 'Mexican food')

for restaurant in [restaurant_1, restaurant_2, restaurant_3]:
    restaurant.print_num_served()
    restaurant.add_num_served(25)
    restaurant.add_num_served(10)
    restaurant.print_num_served()
    restaurant.customer_rating(5)
    restaurant.customer_rating(4)
    restaurant.customer_rating(6)
    restaurant.customer_rating(2.5)
    restaurant.customer_rating('5 stars!')
    print()
