class RewardsProgram:
    """This enhanced rewards program tracks customer visits and reward points."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = {}

    def calculate_rewards(self, restaurant, food_bill):
        # I round down because the exercise says points should be whole numbers.
        points = int(food_bill)
        self.rewards_points[restaurant] = self.rewards_points.get(restaurant, 0) + points
        return points

    def visit_rest(self, restaurant, food_bill):
        if restaurant not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant)
        points = self.calculate_rewards(restaurant, food_bill)
        print(f"Points for this visit: {points}")
        print(f"Total rewards points earned at {restaurant}: {self.rewards_points[restaurant]}")
        print(f"Thank you for visiting {restaurant}!")


customer = RewardsProgram('Mohamed Mouatakid', '202-555-0101', 'mohamed@example.com')
customer.visit_rest('Marrakech Grill', 27.85)
customer.visit_rest('Marrakech Grill', 15.20)
customer.visit_rest('Pasta House', 40.90)
print(customer.restaurants_visited)
print(customer.rewards_points)
