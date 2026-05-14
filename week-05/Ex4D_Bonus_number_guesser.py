

numbers = list(range(1, 11))
number_set = set(numbers)

target_number = numbers[6]

guesses = []
guess_count = 0

print("Guess the number!")
print("Possible numbers are from 1 to 10.")

while True:
    user_input = input("Enter your guess: ")

    if not user_input.isnumeric():
        print("Please enter a number only.")
        continue

    guess = int(user_input)

    if guess not in number_set:
        print("That number is outside the possible range.")
        continue

    guesses.append(guess)
    guess_count = guess_count + 1

    if guess < target_number:
        print("Higher")
    elif guess > target_number:
        print("Lower")
    else:
        print("Correct!")
        break

print(f"You guessed the number in {guess_count} guesses.")
print(f"Your guesses were: {guesses}")

if guess_count < 5:
    print("You're awesome!")
