from random import randint

import Score


def generate_number(difficulty):
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user():
    while True:
        user_input = input("Please guess the number:")
        if user_input.isdigit():
            guess = int(user_input)
            break
        else:
            print("Please enter a number and not a string")
            pass
    return guess


def compare_results(number_given_by_user,secret_num):
    if secret_num != number_given_by_user:
        return False
    else:
        return True


def play(diff):
    secret_number = generate_number(diff)
    num_given = get_guess_from_user()
    result = compare_results(num_given,secret_number)
    if result:
        Score.add_score(diff)
        print(f"Congrats, you guessed right - the secret number was: {secret_number}")
    else:
        print(f"Better luck next time - You guessed {num_given} but the secret number was: {secret_number}")

