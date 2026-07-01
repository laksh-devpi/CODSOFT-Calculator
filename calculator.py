def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def main():
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("\n❌ Please enter valid numbers.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        result = add(num1, num2)
        print(f"\nResult: {num1} + {num2} = {result}")

    elif choice == "2":
        result = subtract(num1, num2)
        print(f"\nResult: {num1} - {num2} = {result}")

    elif choice == "3":
        result = multiply(num1, num2)
        print(f"\nResult: {num1} × {num2} = {result}")

    elif choice == "4":
        result = divide(num1, num2)
        print(f"\nResult: {num1} ÷ {num2} = {result}")

    else:
        print("\n❌ Invalid choice.")


if __name__ == "__main__":
    main()