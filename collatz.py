def collatz_conjecture(x):
    # Validation: Ensure the number is a positive integer
    if x <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    print(f"Starting value: {x}")
    step = 0

    # The cycle continues until x reaches 1
    while x != 1:
        step += 1
        old_x = x

        if x % 2 == 0:
            # If even, divide by 2
            x = x // 2
            print(f"Step {step}: {old_x} is even. Formula: {old_x} / 2 = {x}")
        else:
            # If odd, multiply by 3 and add 1
            x = 3 * x + 1
            print(f"Step {step}: {old_x} is odd. Formula: (3 * {old_x}) + 1 = {x}")

    print(f"\nProcess finished. Total steps taken: {step}")


# This part runs the script when you execute the file
if __name__ == "__main__":
    try:
        user_input = int(input("Enter a positive integer to start: "))
        collatz_conjecture(user_input)
    except ValueError:
        print("Invalid input. Please enter a whole number.")
