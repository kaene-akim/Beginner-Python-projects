def show_definition():
    print("""
Body Mass Index (BMI) is a screening tool used to estimate body fat
based on a person's height and weight.

Formula:
BMI = mass / height²

BMI is not a diagnosis, but it can indicate whether someone may be
underweight, at a healthy weight, overweight, or obese.
""")


def calculate_bmi(mass, height):
    return mass / (height ** 2)


def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "Consider discussing nutrition with a healthcare professional."
    elif bmi < 25:
        return "Healthy Weight", "Keep up the good habits."
    elif bmi < 30:
        return "Overweight", "Consider reviewing your diet and activity levels."
    elif bmi < 35:
        return "Class I Obesity", "Consider seeking professional guidance."
    elif bmi < 40:
        return "Class II Obesity", "Professional support is strongly recommended."
    else:
        return "Class III Obesity", "Professional medical guidance is strongly recommended."


def bmi_check():
    while True:
        try:
            mass = float(input("Mass (kg): "))
            height = float(input("Height (m): "))

            if mass <= 0 or height <= 0:
                print("Mass and height must be positive values.\n")
                continue

            bmi = calculate_bmi(mass, height)

            category, advice = classify_bmi(bmi)

            print("\n" + "-" * 40)
            print(f"BMI: {bmi:.1f}")
            print(f"Category: {category}")
            print(advice)
            print("-" * 40 + "\n")

            break

        except ValueError:
            print("Please enter valid numbers.\n")


def show_reference_table():
    print("""
BMI Reference Table
-------------------
Below 18.5     : Underweight
18.5 - 24.9    : Healthy Weight
25.0 - 29.9    : Overweight
30.0 - 34.9    : Class I Obesity
35.0 - 39.9    : Class II Obesity
40.0 and above : Class III Obesity
""")


while True:
    menu = input(
        "\n" + "=" * 50 +
        "\n           BMI CALCULATOR" +
        "\n" + "=" * 50 +
        "\n1. BMI Definition"
        "\n2. Check BMI"
        "\n3. BMI Reference Table"
        "\n4. Quit"
        "\n\nSelect option: "
    )

    if menu == "1":
        show_definition()

    elif menu == "2":
        bmi_check()

    elif menu == "3":
        show_reference_table()

    elif menu == "4":
        print("Goodbye.")
        break

    else:
        print("Invalid option. Please try again.")