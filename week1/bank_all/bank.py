import time
from values_bank import (
    values,
    total_values,
)

def main():
    greeting = input("Greeting: ").strip()
    greeting_lower = greeting.lower()

    if greeting_lower == "hello":
        result = values()["hello"]
    elif greeting_lower.startswith("h"):
        result = values()["h"]
    else:
        result = values()["nothing"]

    print(result)
    dados = values()

    time.sleep(1)
    
    continue_prompt = input("Do you want to continue? (yes/no): ").strip().lower()
    while continue_prompt not in ["yes", "no"]:
        continue_prompt = input("Please enter 'yes' or 'no': ").strip().lower()
    if continue_prompt == "yes":
        main()
    else: 
        print("Total values:", total_values())
        print("Goodbye!")

main()
