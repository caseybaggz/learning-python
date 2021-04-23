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
    url = "https://pokeapi.co/api/v2/pokemon/"
    formatted_choice = choice.lower()
    req = requests.get(f"{url}{formatted_choice}")

    if req.status_code == requests.codes.ok:
        print(req.json())
    else:
        req.raise_for_status()


# Program

if __name__ == "__main__":
    start()
    choice = get_choice()
    fetch_pokemon(choice)
