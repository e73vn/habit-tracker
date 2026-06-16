import json

def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file)

def load_habits():
    try:
        with open("habits.json", "r") as file:
            return json.load(file)
    except:
        return []
