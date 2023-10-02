import requests


def get_money_interval(difficulty):
    url = "https://currency-exchange.p.rapidapi.com/exchange"

    querystring = {"from": "USD", "to": "ILS", "q": "1.0"}

    headers = {
        "X-RapidAPI-Key": "3e82e287dbmsh8d4753514783692p1dfb0cjsncb3b02825609",
        "X-RapidAPI-Host": "currency-exchange.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    exchange_rate = response.json()


    if difficulty == 5:
        money_interval = [
            exchange_rate - (exchange_rate * 0.1),
            exchange_rate + (exchange_rate * 0.1)
        ]
    elif difficulty == 4:
        money_interval = [
            exchange_rate - (exchange_rate * 0.2),
            exchange_rate + (exchange_rate * 0.2)
        ]
    elif difficulty == 3:
        money_interval = [
            exchange_rate - (exchange_rate * 0.3),
            exchange_rate + (exchange_rate * 0.3)
        ]
    elif difficulty == 2:
        money_interval = [
            exchange_rate - (exchange_rate * 0.4),
            exchange_rate + (exchange_rate * 0.4)
        ]
    elif difficulty == 1:
        money_interval = [
            exchange_rate - (exchange_rate * 0.5),
            exchange_rate + (exchange_rate * 0.5)
        ]

    money_interval.append(exchange_rate) # append the current exchange rate to position 2 in the array
    return money_interval


def get_guess_from_user():
    guess = float(input("Please guess the current exchange rate of USD to ILS: "))
    return guess


def play(diff):
    correct_guess_array = get_money_interval(diff)
    lower_guess = correct_guess_array[0]
    higher_guess = correct_guess_array[1]
    exchange_rate = correct_guess_array[2]
    user_guess = get_guess_from_user()
    if lower_guess <= user_guess <= higher_guess:
        print(f"You Win, Your Guess:\n{user_guess}\nThe current exchange rate is {exchange_rate}")
        return True
    else:
        print(f"You Lose, Your Guess:\n{user_guess}\nThe current exchange rate is {exchange_rate}")
        return False
