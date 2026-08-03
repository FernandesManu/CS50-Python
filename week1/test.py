running = True

while running:
    # Get input from the user
    command = input("Enter a command (start, stop, status, quit): ").strip().lower()
    
    match command:
        case "start":
            print("System started.")
        case "stop":
            print("System stopped.")
        case "status":
            print("System is running normally.")
        case "quit":
            print("Exiting program...")
            running = False  # Breaks the while loop condition
        case _:
            print("Unknown command. Please try again.")  # Handles invalid inputs
