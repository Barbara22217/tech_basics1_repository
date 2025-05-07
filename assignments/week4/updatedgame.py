import random
import time

MIN_NUMBER = 1
MAX_NUMBER = 100
DELAY_SECONDS = 1

DIFFICULTY_SETTINGS = {
    'easy': 10,
    'medium': 7,
    'hard': 5
}


def welcome_player():
    print("Welcome to the Guess the Number Game!")
    name = input("What's your name? ").strip()
    print(f"Hi {name}!")

    age = int(input("How old are you? "))
    if age < 6:
        print("You are too young to play.")
        return None
    return name


def choose_difficulty():
    print("\nChoose a difficulty: easy / medium / hard")
    while True:
        choice = input("Enter difficulty: ").lower()
        if choice in DIFFICULTY_SETTINGS:
            return DIFFICULTY_SETTINGS[choice]
        print("Invalid choice. Please type: easy, medium, or hard.")


def generate_number():
    print("Generating a secret number...")
    for _ in range(3):
        time.sleep(DELAY_SECONDS)
        print(".")
    return random.randint(MIN_NUMBER, MAX_NUMBER)


def get_guess():
    while True:
        try:
            guess = int(input(f"Guess a number between {MIN_NUMBER} and {MAX_NUMBER}: "))
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
            print("Out of range!")
        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game(secret_number, max_attempts):
    attempts = 0
    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        if guess < secret_number:
            print("Go higher!")
        elif guess > secret_number:
            print("Go lower!")
        else:
            print(f"🎉 You got it in {attempts} attempts!")
            return max_attempts - attempts + 1  # Score based on remaining attempts

    print(f"😞 You lose... The number was {secret_number}.")
    return 0


def main():
    player_name = welcome_player()
    if not player_name:
        return

    max_attempts = choose_difficulty()
    secret_number = generate_number()

    score = play_game(secret_number, max_attempts)
    print(f"\nYour final score is: {score}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
