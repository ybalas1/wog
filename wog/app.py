import current_roullete
import guess_game
import memory_gamee

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
            # Check username does not start with number
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
    max_games_to_choose = 3 # max games to choose\
    max_difficutly_to_choose = 5  # max games to choose

    # Prints start play message
    print(f"Please choose a game to play:\n"
           "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.\n"
           "2. Guess Game - guess a number and see if you chose like the computer.\n"
           "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    # Get the number and prform validations
    while True:
        try:
            game_num_chosen = int(input("Please enter you desired game number: ")) # Choose num
            # Check if its integer
            if type(game_num_chosen) != int:
                raise ValueError("Please insert a number and not a string")
            # check if game chosen is within range
            if game_num_chosen < 1 or game_num_chosen > max_games_to_choose:
                raise ValueError(f"No such game")
            break

        except ValueError as ve:
            print(f"Error: {ve}\n\n")

    print(f"\nGreat choice!\n")
    game = game_num_chosen

    while True:
        try:
            diff_level_chosen = int(input("Please enter you desired difficutly between 1-5: ")) # Choose difficualty

            # Check if its integer
            if type(diff_level_chosen) != int:
                raise ValueError("Please insert a number and not a string")
            # check if game chosen is within range
            if diff_level_chosen < 1 or diff_level_chosen > max_difficutly_to_choose:
                raise ValueError(f"No such difficutly")
            break
        except ValueError as ve:
            print(f"Error: {ve}\n\n")

    diff_chosen = diff_level_chosen
    print(f"\nStarting \"{game_dict[game_num_chosen -1]}\"\n"
          f"Difficulty chosen: {diff_chosen}\n"
          f"Good Luck!")

    if game_num_chosen == 1:
        memory_gamee.play(diff_chosen)
    elif game_num_chosen == 2:
        guess_game.play(diff_chosen)
    elif game_num_chosen == 3:
        current_roullete.play(diff_chosen)



