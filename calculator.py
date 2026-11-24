"""
CodeOrbit Tech - Task 1: Simple Calculator
Performs addition, subtraction, multiplication, and division.
"""

def calculate():
    print("\n=== SIMPLE CALCULATOR ===")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = input("Enter choice (1-4): ").strip()
        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            return

        # Convert the user's input into numbers.
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform the selected arithmetic operation.
        if choice == "1":
            result = num1 + num2
            symbol = "+"
        elif choice == "2":
            result = num1 - num2
            symbol = "-"
        elif choice == "3":
            result = num1 * num2
            symbol = "*"
        else:
            # Division by zero is not allowed.
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                return
            result = num1 / num2
            symbol = "/"

        print(f"Result: {num1:g} {symbol} {num2:g} = {result:g}")

    except ValueError:
        # This handles inputs that cannot be converted to numbers.
        print("Invalid input. Please enter numeric values.")
    except Exception as error:
        print(f"An unexpected error occurred: {error}")


if __name__ == "__main__":
    calculate()
