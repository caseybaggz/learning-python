import random

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

options = {
    ROCK: {"id": "1", "label": "Rock"},
    PAPER: {"id": "2", "label": "Paper"},
    SCISSORS: {"id": "3", "label": "Scissors"},
}


def setup_chioces():
    choices = []
    for option_item in options.keys():
        choices.append(options[option_item].get("id"))
    return choices


def start_game(choices):
    ai = random.choice(choices)
    user = input(
        "ROCK, PAPER, SCISSORS!!!!\nChoose Your Option...\n\n1. Rock\n2. Paper\n3. Scissors\n"
    )
    return {"ai": ai, "user": user}


def determine_win(players, choices):
    user = players.get("user")
    ai = players.get("ai")

    if user not in choices:
        print("You must choose either 1, 2, or 3 as an option.")
        return

    if ai == user:
        print("Tie!")
    elif ai == options.get(ROCK)["id"] and user == options.get(SCISSORS)["id"]:
        print("Computer wins...")
    elif ai == options.get(SCISSORS)["id"] and user == options.get(PAPER)["id"]:
        print("Computer wins...")
    else:
        print("YOU WIN!")

    print("You chose " + user + ". The computer chose " + ai + ".")


# Run Game

choices = setup_chioces()
players = start_game(choices)

determine_win(players, choices)
