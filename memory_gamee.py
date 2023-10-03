import time

import Score
import Utils
from random import randint


def generate_sequence(diff):
    num_array = []
    for x in range(diff):
        x = randint(1, 101)
        num_array.append(x)
    print(f"Remember the following sequence (Hurry up, you have only 5 seconds):\n {', '.join(map(str, num_array))}")
    time.sleep(5)
    Utils.screen_cleaner()
    return num_array


def get_list_from_user(input_multiplier):
    user_input_array = []
    for x in range(input_multiplier):
        suffix = 'th'
        if 1 <= (x + 1) % 10 <= 3 and (x + 1) % 100 not in [11, 12, 13]:
            suffix = ['st', 'nd', 'rd'][(x + 1) % 10 - 1]
        num = int(input(f"Please enter the {x + 1}{suffix} number: "))
        user_input_array.append(num)
    return user_input_array


def is_list_equal(generated_list, user_list):
    generated_list_sorted = sorted(generated_list)
    user_list_sorted = sorted(user_list)

    if generated_list_sorted == user_list_sorted:
        print("Great Job")
        return True
    else:
        print(f"You Failed\nYour Guess: {user_list_sorted}\nThe correct number were: {generated_list_sorted}")
        return False


def play(diff):
    gen_arr = generate_sequence(diff)  # Save generated array
    user_arr = get_list_from_user(diff)  # Save user array
    game_result = is_list_equal(gen_arr, user_arr)
    # If user won add score
    if game_result:
        Score.add_score(diff)
    else:
        pass

