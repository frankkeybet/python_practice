import random

print("Welcome to the Number Guessing Game!")

# Main game loop
while True:
    secret_number = random.randint(1, 10)
    print("\nI'm thinking of a number between 1 and 10. Can you guess it?")
    
    attempts = 0  # Counter for number of guesses
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        match guess:
            case _ if guess == secret_number:
                print(f"🎉 Congratulations, you guessed it in {attempts} tries!")
                break
            case _ if guess > secret_number:
                print("📈 Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("📉 Nope, your guess is a bit low. Give it another shot!")
    
    # Ask if the user wants to play again
    play_again = input("\nPlay again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye 👋")
        break
