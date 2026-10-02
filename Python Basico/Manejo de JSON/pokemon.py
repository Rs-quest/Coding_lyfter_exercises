import json


def get_pokemon():
    name = input("Name: ")
    pokemon_type = input("Type: ")
    level = int(input("Level: "))
    weight_kg = float(input("Weight (kg): "))
    is_shiny = input("Is shiny? (yes/no): ").lower() == "yes"
    held_item = input("Held item: ")

    skills = []

    for i in range(4):
        skill = input(f"Skill {i + 1}: ")
        skills.append(skill)

    stats = {
        "hp": int(input("HP: ")),
        "attack": int(input("Attack: ")),
        "defense": int(input("Defense: ")),
        "sp_attack": int(input("Special Attack: ")),
        "sp_defense": int(input("Special Defense: ")),
        "speed": int(input("Speed: "))
    }

    return {
        "name": name,
        "type": pokemon_type,
        "level": level,
        "weight_kg": weight_kg,
        "is_shiny": is_shiny,
        "held_item": held_item,
        "skills": skills,
        "stats": stats
    }


def add_pokemon(pokemon_list):
    new_pokemon = get_pokemon()

    while True:
        answer = input("Do you want to modify anything? (yes/no): ").lower()

        if answer == "yes":
            new_pokemon = get_pokemon()
        else:
            break

    pokemon_list.append(new_pokemon)


def save_pokemon(pokemon_list):
    with open("pokemon.json", "w", encoding="utf-8") as file:
        json.dump(pokemon_list, file, indent=4)


def main():
    with open("pokemon.json", "r", encoding="utf-8") as file:
        pokemon_list = json.load(file)

    add_pokemon(pokemon_list)

    save_pokemon(pokemon_list)


main()