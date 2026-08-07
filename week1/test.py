# Get the input from the user
user_input = input("Enter some text: ")

# Check if "hello" is in the lowercase version of the input
if "hello" in user_input.lower():
    print("Yes, the input contains 'hello'!")
else:
    print("No, 'hello' was not found.")
