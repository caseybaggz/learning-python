import requests


def start():
    print(
        """
    Welcome to Pokémon Finder!
    --------------------------
  """
    )


def get_choice():
    return input("Which Pokémon do you want to know about...\n")


def fetch_pokemon(choice):
    req = requests.get("https://pokeapi.co/api/v2/pokemon/" + choice.lower())

    if req.status_code == requests.codes.ok:
        print(req.text)
    else:
        req.raise_for_status()


# Run program

start()
choice = get_choice()
fetch_pokemon(choice)
