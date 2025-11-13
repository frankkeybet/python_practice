secret_number = 8
guess_count = 0
guess = 0
while guess != secret_number:
    guess_count += 1
    guess = int(input("Enter your guess between 1 and 10: "))
print(f"You guessed it in {guess_count} tries!")