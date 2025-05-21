def choose_game_mode():
    print("\nChoose Game Mode:")
    print("1. Solo (one character)")
    print("2. Party (multiple characters)")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == '1':
        return "solo", 1
    elif choice == '2':
        size = input("How many characters in your party? (2-4): ").strip()
        if size.isdigit() and 2 <= int(size) <= 4:
            return "party", int(size)
        else:
            print("Invalid party size. Defaulting to 2.")
            return "party", 2
    else:
        print("Invalid choice. Defaulting to solo mode.")
        return "solo", 1