import json

# Get the sound of the corresponding animal
def get_animal_sound(animal_name: str) -> str:
    sounds = {
        "dog": "bark",
        "cat": "meow",
        "cow": "moo",
        "rat": "pipi",
        "alien": "KILL",
    }

    return sounds.get(animal_name, "Unknown animal.")


with open('test.json', 'r') as file:
    date = json.load(file)

animal = date.get("animal", "Unknown.")

print(get_animal_sound(animal_name=animal))
