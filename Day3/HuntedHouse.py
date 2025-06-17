print("You wake up in a creepy haunted house...")
choice1 = input("There are two paths: one to the basement and one to the attic. choose 'basement' or 'attic': ").lower()
if choice1 == "attic":
    print("You climb up the creaky stairs into the dusty attic.")
    print("You see an old wardrobe and a window.")
    choice2 = input("Do you want to open the 'wardrobe' or look out the 'window'? ").lower()
    if choice2 == "wardrope":
        print("Inside the wardrobe you find three keys: one gold, one silver, and one rusty.")
        choice3 = input("Which key do you take? 'gold', 'silver', or 'rusty'? ").lower()
        if choice3 == "gold":
            print("The gold key unlocks a secret passage that leads you to safety. You win!")
        elif choice3 == "silver":
            print("The silver key opens a trapdoor that drops you into the basement. Game over.")
        elif choice3 == "rusty":
            print("The rusty key breaks in the lock, trapping you in the attic forever. Game over.")
        else:
            print("Invalid choice. You are trapped forever.")
    elif choice2 == "window":
        print("You look out the window and see a ghostly figure staring back at you.")
        print("You scream and fall back, hitting your head. Game over.")
elif choice1 == "basement":
    print("You descend into the dark, damp basement. There's a glowing chest.")
    choice2 = input("Do you 'open the chest' or 'go back'? ").lower()
    if choice2 == "open the chest":
        print("you find three keys: one gold, one silver, and one rusty.")
        choice3 = input("Which key do you take? 'gold', 'silver', or 'rusty'? ").lower()
        if choice3 == "gold":
            print("The gold key unlocks a secret passage that leads you to safety. You win!")
        elif choice3 == "silver":
            print("The silver key opens a trapdoor that drops you into the attic. Game over.")
        elif choice3 == "rusty":
            print("The rusty key breaks in the lock, trapping you in the basement forever. Game over.")
        else:
            print("Invalid choice. You are trapped forever.")
    elif choice2 == "go back":
        print("You decide to go back upstairs, but the stairs collapse behind you.")
        print("You are trapped in the basement forever. Game over.")