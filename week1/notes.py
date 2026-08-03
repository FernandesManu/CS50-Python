import time

while True:
    name = input("Enter your name: ")

    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
            break
        case "Draco":
            print("Slytherin")
            break
        case _:
            print("Unknown house")
            time.sleep(1) 
            print("Please try again.")