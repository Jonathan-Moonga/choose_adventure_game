def college_admissions():
    print("\nWelcome to the College Admissions Track. Have fun!")
    score = 0

    name = input("Please type your name: ")
    print(f"Welcome {name}, to this adventure!")
    
    answer = input("You are in grade 10. Do you join a school club or focus only on academics? (club/academics): ").lower()
    if answer == "club":
        print("Great choice! Joining a club builds your profile. +1 point.")
        score += 1
    elif answer == "academics":
        print("Focusing only on academics limits your profile. No points.")
    else:
        print("Not a valid option. Moving on.")

    answer = input("It's grade 11 now. Do you start writing your personal statement? (yes/no/maybe): ").lower()
    if answer == "yes":
        print("Excellent! Starting early gives you more time to perfect it. +1 point.")
        score += 1
    elif answer == "no":
        print("Waiting might make it rushed later. No points.")
    elif answer == "maybe":
        print("Uncertainty isn't helpful here. No points.")
    else:
        print("Not a valid option. Moving on.")

    answer = input("In grade 12, do you finalize your college list early? (yes/no/maybe): ").lower()
    if answer == "yes":
        print("Good planning! It helps you focus on applications. +1 point.")
        score += 1
    elif answer == "no":
        print("You might miss some deadlines. No points.")
    elif answer == "maybe":
        print("Uncertainty could cost you. No points.")
    else:
        print("Not a valid option. Moving on.")

    print(f"\nTrack Complete! Your score for College Admissions: {score}/3")

def children_outdoor_safety():
    print("\nWelcome to the Children Outdoor Safety Track. Stay safe!")
    score = 0

    answer = input("You see a stranger offering candy. Do you take it? (yes/no/maybe): ").lower()
    if answer == "no":
        print("Good job! It's important to be cautious. +1 point.")
        score += 1
    elif answer in ["yes", "maybe"]:
        print("That's unsafe! No points.")
    else:
        print("Not a valid option. Moving on.")

    answer = input("Do you play near a busy street without an adult? (yes/no/maybe): ").lower()
    if answer == "no":
        print("Smart decision! Safety first. +1 point.")
        score += 1
    else:
        print("That’s risky. No points.")

    answer = input("Do you inform an adult before going outside? (yes/no/maybe): ").lower()
    if answer == "yes":
        print("Great! It's important to inform adults. +1 point.")
        score += 1
    else:
        print("That could lead to trouble. No points.")

    print(f"\nTrack Complete! Your score for Children Outdoor Safety: {score}/3")

def grocery_shopping_for_children():
    print("\nWelcome to the Grocery Shopping Track. Let's learn to shop smart!")
    score = 0

    answer = input("Do you make a shopping list before going to the store? (yes/no/maybe): ").lower()
    if answer == "yes":
        print("Good planning! +1 point.")
        score += 1
    else:
        print("Shopping without a list can lead to overspending. No points.")

    answer = input("Do you compare prices before buying items? (yes/no/maybe): ").lower()
    if answer == "yes":
        print("Smart move! Comparing prices saves money. +1 point.")
        score += 1
    else:
        print("You might overspend without comparing prices. No points.")

    answer = input("Do you check expiration dates before buying items? (yes/no/maybe): ").lower()
    if answer == "yes":
        print("Great! This prevents waste and ensures freshness. +1 point.")
        score += 1
    else:
        print("You might end up with spoiled items. No points.")

    print(f"\nTrack Complete! Your score for Grocery Shopping: {score}/3")

def main():
    print("Welcome to The Life Game!")
    print("Choose a track:")
    print("1. College Admissions")
    print("2. Children Outdoor Safety")
    print("3. Grocery Shopping for Children")

    choice = input("Enter the number of your chosen track: ")
    if choice == "1":
        college_admissions()
    elif choice == "2":
        children_outdoor_safety()
    elif choice == "3":
        grocery_shopping_for_children()
    else:
        print("Invalid choice. Exiting the game.")

if __name__ == "__main__":
    main()
