import current_roullete
import guess_game
import memory_gamee


def get_valid_integer_input(prompt, min_value, max_value):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            input_value = int(user_input)

            if min_value <= input_value <= max_value:
                return input_value  # Return the valid integer input

        print(f"Invalid input. Please enter a valid integer between {min_value} and {max_value}.")



diff_chosen = 0

game_dict = ["Memory Game", "Guess Game", "Currency Roulette"]


def welcome():
    while True:
        try:
            # Get Username
            username = input("Please enter your full name: ")
            # Check len of name is > 1
            if len(username) < 2:
                raise ValueError("Username must be at least 2 characters long")
            # Check username does not start with a number
            if username[0].isdigit():
                raise ValueError("Username must start with a letter")
            # Check username is not null
            if len(username) < 1:
                raise ValueError("Username cannot be null")
            break
        except ValueError as ve:
            print(f"Error: {ve}\n\n")

    print(f"\nHi {username} and welcome to the World of Games: The Epic Journey\n")


def start_play():
    max_games_to_choose = 3
    max_difficutly_to_choose = 5

    print(f"Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
          "2. Guess Game - guess a number and see if you chose like the computer.\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    # Get the game number and validate it
    game_num_chosen = get_valid_integer_input("Please enter your desired game number: ", 1, max_games_to_choose)

    print(f"\nGreat choice!\n")
    game = game_num_chosen

    # Get the difficulty level and validate it
    diff_chosen = get_valid_integer_input("Please enter your desired difficulty between 1-5: ", 1, max_difficutly_to_choose)

    print(f"\nStarting \"{game_dict[game_num_chosen - 1]}\"\n"
          f"Difficulty chosen: {diff_chosen}\n"
          f"Good Luck!")

    if game_num_chosen == 1:
        memory_gamee.play(diff_chosen)
    elif game_num_chosen == 2:
        guess_game.play(diff_chosen)
    elif game_num_chosen == 3:
        current_roullete.play(diff_chosen)

