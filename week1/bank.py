from values_bank import values

def main():
    greeting = input("Greeting: ")

    if greeting:
        data = values()
        if "hello" in greeting.lower():
            print("Hello to you too!")
            print("Valores:", data)
        else:
            print("Greeting não reconhecido.")
    else:
        print("No greeting provided.")


main()
