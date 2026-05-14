import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
            'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

# I use choice because the team only needs one product of the day.
product_of_day = random.choice(products)
print(f"Product of the Day: {product_of_day}")

# I use sample because I need 3 different products and I do not want duplicates.
survey_products = random.sample(products, 3)
print(f"Products for usability survey: {survey_products}")

# shuffle changes the original list in place, so I print products after shuffling.
random.shuffle(products)
print(f"Randomized presentation order: {products}")

# randint gives me one random whole number between 50 and 300.
daily_transactions = random.randint(50, 300)
print(f"Simulated daily transaction count: {daily_transactions}")
