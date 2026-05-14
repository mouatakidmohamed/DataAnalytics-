cust_list = []

class RewardsProgram:
    """This class stores customer rewards profile information."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        # I append to the global list so previous customers are not erased.
        cust_list.append((self.cust_name, self.phone, self.email))


customers = [
    RewardsProgram('Mohamed Mouatakid', '202-555-0101', 'mohamed@example.com'),
    RewardsProgram('Amina Ali', '202-555-0102', 'amina@example.com'),
    RewardsProgram('John Doe', '202-555-0103', 'john@example.com')
]

for customer in customers:
    customer.profile()
    customer.thank_you()
    customer.add_to_cust_list()
    print()

print(cust_list)
