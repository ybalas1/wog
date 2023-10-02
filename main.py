import requests

import Utils
import app
from app import diff_chosen

difficulty = diff_chosen
while True:
    app.welcome()
    app.start_play()
    if int(input("Do you want to play again?\n Enter 1 to play again \nEnter 2 to end the game")) == 1:
        Utils.screen_cleaner()
    else:
        print("Good Game, have a great rest of your day")
        break

