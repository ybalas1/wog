from random import randint


def generate_number(difficulty):
    secret_number = randint(1, difficulty)
    return secret_number


def get_guess_from_user():
    guess = int(input("Please guess the number: "))
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
        print(f"Congrats, you guessed right - the secret number was: {secret_number}")
    else:
        print(f"Better luck next time - You guessed {num_given} but the secret number was: {secret_number}")

