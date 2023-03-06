import sys

from poke_api   import PokeMon
from pastebin_api   import post_new_paste

def main():

    Pokemon = Pokemon_name()
    Pokemon_Info = PokeMon(Pokemon)

    Pokemon_Paste(Pokemon, Pokemon_Info)


def Pokemon_name():

    if len(sys.argv) < 2:
        print('Pokemon Name: ')
        exit()

    return sys.argv[1]

def Pokemon_Paste(Pokemon_name, Pokemon_Info):

    title = f"{Pokemon_name.capitalize()}'s abilities"
    Abilities = []

    for Ability in Pokemon_Info['Abilities']:

        Abilities.append(Ability["Ability"]["Name"])

        body = "\n".join(Abilities)
        expiration = "1M"
        Publicity_listed = False

        post_new_paste(title, body, expiration, Publicity_listed)

    return 


if __name__ == "__main__":
    main()