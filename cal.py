def calculator():
    print("Calculator!")

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Quit")

        choice = input("Enter your choice")

        if choice == "5":
            print("\nThank you for using the calculator. Goodbye!")
            break

        if choice in ("1", "2", "3", "4"):
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    res = num1 + num2
                    print(f"\nResult: {num1} + {num2} = {res}")
                elif choice == "2":
                    res = num1 - num2
                    print(f"\nResult: {num1} - {num2} = {res}")
                elif choice == "3":
                    res = num1 * num2
                    print(f"\nResult: {num1} * {num2} = {res}")
                elif choice == "4":
                    if num2 != 0:
                        res = num1 / num2
                        print(f"\nResult: {num1} / {num2} = {res}")
                    else:
                        print("\nError: Cannot divide by zero.")
            except ValueError:
                print("\nInvalid input. Please enter numeric values only.")
        else:
            print("\nInvalid choice. Please select a valid operation.")

calculator()
