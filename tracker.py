from storage import save_habits, load_habits

habits = load_habits()

while True:
    print("\nHabit Tracker")
    print("1. Add habit")
    print("2. View habits")
    print("3. Quit")

    choice = input("> ")

    if choice == "1":
        habit = input("New habit: ")
        habits.append(habit)
        print("Added!")

    elif choice == "2":
        for habit in habits:
            print("-", habit)

    elif choice == "3":
        break
