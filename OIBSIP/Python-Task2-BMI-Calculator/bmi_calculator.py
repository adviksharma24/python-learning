print("=" * 50)
print("              BMI CALCULATOR")
print("=" * 50)

while True:
    print("\nEnter your details")
    print("-" * 50)

    # Get weight
    while True:
        try:
            weight = float(input("Enter your weight (kg): "))

            if weight <= 0:
                print("Please enter a weight greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Get height
    while True:
        try:
            height = float(input("Enter your height (meters): "))

            if height <= 0:
                print("Please enter a height greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Calculate BMI
    bmi = weight / (height * height)

    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
        message = "You may need to improve your nutrition."
    elif bmi < 25:
        category = "Normal weight"
        message = "Great! Your BMI is in the normal range."
    elif bmi < 30:
        category = "Overweight"
        message = "Consider maintaining a healthy diet and activity level."
    else:
        category = "Obese"
        message = "Consider focusing on a healthy lifestyle."

    # Display result
    print("\n" + "=" * 50)
    print("                 BMI RESULT")
    print("=" * 50)
    print(f"Your BMI     : {bmi:.2f}")
    print(f"Category     : {category}")
    print(f"Information  : {message}")
    print("=" * 50)

    # Ask for another calculation
    while True:
        choice = input("\nWould you like to calculate again? (y/n): ").lower()

        if choice == "y":
            break
        elif choice == "n":
            print("\nThank you for using the BMI Calculator!")
            print("Have a healthy day!")
            print("=" * 50)
            exit()
        else:
            print("Please enter only 'y' or 'n'.")