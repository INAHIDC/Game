import random

def play_game():
    score = 0
    play_again = True

    print("Looks like someone just woke up!")

    while play_again:
        difficulty = input("pick a difficulty level (easy, medium, hard): ")

        if difficulty.lower() not in ['easy', 'medium', 'hard']:
            print("Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")
            continue

        max_attempts = {'easy': 10, 'medium': 7, 'hard': 5}
        number = random.randint(1, 100)
        attempts = 0

        print(f"You have {max_attempts[difficulty.lower()]} attempts to guess the number.")

        while attempts < max_attempts[difficulty.lower()]:
            guess = input("Enter your guess (1-100), or 'q' to quit: ")

            if guess.lower() == 'q':
                print("Quitting the game. See you next time!")
                play_again = False
                break

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input. Please enter a number or 'q' to quit.")
                continue

            attempts += 1

            if guess < number:
                print("Silence! Too low! Keep trying!")
            elif guess > number:
                print("Silence! Too high! Keep trying!")
            else:
                print("Silence! Congratulations! You guessed the number!")
                score += 1
                break

        if attempts == max_attempts[difficulty.lower()]:
            print(f"Silence! You have used up all your attempts. The number was {number}.")
        
        if play_again:
            play_again_response = input("Do you want to play again? (yes/no): ")

            if play_again_response.lower() == 'no':
                play_again = False

    print(f"Silence! Your final score is {score}.")
    farewell_achmed()

def introduce_achmed():
    print("Hello, infidels! I am Achmed, the dead terrorist. Let's play a game! if you win i let you live, if you lose...")

def farewell_achmed():
    print("Goodbye, infidels! Until next time.")
 

introduce_achmed()
play_game()
