while True:
    print("\n--- Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Factorial")
    print("Type 'exit' to stop")

    choice = input("Enter your choice: ")

    if choice == "exit":
        print("Calculator terminated.")
        break

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == "3":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == "4":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if b == 0:
            print("Cannot divide by zero.")
        else:
            print("Result =", a / b)

    elif choice == "5":
        n = int(input("Enter a number: "))

        factorial = 1
        i = 1

        while i <= n:
            factorial = factorial * i
            i = i + 1

        print("Factorial =", factorial)

    else:
        print("Invalid choice. Please try again.")