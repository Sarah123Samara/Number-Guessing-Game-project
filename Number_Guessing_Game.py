import random

# Set the initial high score to a value that is significantly large.
high_score = float("inf")

# Display welcome message
print()
print("-----------------------------------")
print("Welcome to the Number Guessing Game")
print("-----------------------------------")
print()


# Function to start a new game
def start_game():
    num = random.randint(1, 50)
    return num


# Main game loop
while True:
    num = start_game()
    attempts = 0

    # Guessing loop
    while True:
        print()
        user_input = input("Guess a number (type 'quit' to exit): ")

        # Check for quitting
        if user_input.lower() == "quit":
            print()
            print("Thank you for playing!")
            print("Goodbye! Hope to see you soon.")
            print()
            exit()

        try:
            user_input = int(user_input)
            attempts += 1

            # Check if input is within range
            if user_input > 50 or user_input < 1:
                print("Your guess is outside the range of numbers. Please try again.")
                print()
            elif user_input > num:
                if user_input - num <= 5:
                    print(
                        "Wait, hold on! Looks like it's your lucky day. Go a little lower."
                    )
                    print()
                else:
                    print(
                        "That's way too far. I think you'd better stick to your day job. It's way lower."
                    )
                    print()
            elif user_input < num:
                if num - user_input <= 5:
                    print(
                        "That's close. Your brain seems to be shining a bit brighter now! Go a little higher."
                    )
                    print()
                else:
                    print(
                        "Nice attempt, but I've seen toddlers with better game skills. It's way higher."
                    )
                    print()
            else:
                print()
                print("Well Done! You got it right.")
                print(f"It took you {attempts} attempt/s to get the correct number.")

                # Update and display high score if beaten
                if attempts < high_score:
                    high_score = attempts
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    # Play again decision loop
    while True:
        print()
        user_decision = input("Would you like to play again? (Enter Yes/No): ").lower()

        if user_decision == "yes":
            print(f"Your best high score is {high_score} attempt/s!")
            print()
            high_score = min(high_score, attempts)
            break
        elif user_decision == "no":
            print()
            print("Thank you for playing!")
            print("Have a nice day.")
            print()
            exit()
        else:
            print("Invalid input. Please enter Yes or No.")

