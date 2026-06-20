from datetime import date
from storage import load_habits, save_habits

habits = load_habits()

while True:
    print("\n1. Add habit")
    print("2. View habits")
    print("3. Delete habit")
    print("4. Mark habit complete")
    print("5. Quit")

    choice = input("> ")

    if choice == "1":
        habit = input("Enter a habit: ")

        if habit == "":
            print("Habit cannot be empty.")
        elif habit in habits:
            print("That habit already exists.")
        else:
            habits[habit] = []
            save_habits(habits)
            print("Added")

    elif choice == "2":
        if not habits:
            print("No habits yet.")
        else:
            for habit, completed_days in habits.items():
                print("-", habit, completed_days)

    elif choice == "3":
        habit = input("Which habit do you want to delete? ")

        if habit in habits:
            del habits[habit]
            save_habits(habits)
            print("Deleted")
        else:
            print("Habit not found.")

    elif choice == "4":
        habit = input("Which habit did you complete? ")
        today = str(date.today())

        if habit in habits:
            if today in habits[habit]:
                print("Already marked complete today.")
            else:
                habits[habit].append(today)
                save_habits(habits)
                print("Marked complete")
        else:
            print("Habit not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
