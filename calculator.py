class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Enter choice(1/2/3/4/5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result is: {calc.add(num1, num2)}")

        elif choice == '2':
            print(f"The result is: {calc.subtract(num1, num2)}")

        elif choice == '3':
            print(f"The result is: {calc.multiply(num1, num2)}")

        elif choice == '4':
            try:
                print(f"The result is: {calc.divide(num1, num2)}")
            except ValueError as e:
                print(e)

        else:
            print("Invalid input. Please select a valid operation.")