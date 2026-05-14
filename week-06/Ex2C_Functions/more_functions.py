def display_mailing_label(name, address, city, state, zip_code):
    # I print the information like a real mailing label.
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")


def add_numbers(*numbers):
    # *numbers lets me send one number or many numbers to the same function.
    result = sum(numbers)
    expression = " + ".join(str(n) for n in numbers)
    print(f"{expression} = {result}")


def display_receipt(total_due, amount_paid):
    # I subtract total due from amount paid to find the change or balance.
    difference = amount_paid - total_due
    print(f"Total Due: ${total_due:.2f}")
    print(f"Amount Paid: ${amount_paid:.2f}")
    if difference >= 0:
        print(f"Change Due: ${difference:.2f}")
    else:
        print(f"Remaining Balance: ${abs(difference):.2f}")


def display_mailing_label2(name, address1, city, state, zip_code, address2=''):
    # This bonus version allows an optional second address line.
    print(name)
    print(address1)
    if address2:
        print(address2)
    print(f"{city}, {state} {zip_code}")


def display_receipt2(amount_paid, *totals_due):
    # This bonus version can add multiple balances before calculating payment.
    total_due = sum(totals_due)
    display_receipt(total_due, amount_paid)


print("--- Mailing Labels ---")
display_mailing_label('Mohamed Mouatakid', '123 Main St', 'Washington', 'DC', '20001')
print()
display_mailing_label('Jane Smith', '456 Park Ave', 'Baltimore', 'MD', '21201')

print("\n--- Add Numbers ---")
add_numbers(5)
add_numbers(5, 10)
add_numbers(5, 10, 15, 20)

print("\n--- Receipts ---")
display_receipt(25.00, 30.00)
print()
display_receipt(25.00, 25.00)
print()
display_receipt(25.00, 20.00)
