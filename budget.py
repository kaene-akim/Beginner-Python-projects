budget = {}

def calculate_budget():
    net_income = float(input("Monthly income (BWP): "))

    total_needs = 0

    while True:
        need = input("Insert need (blank or 'quit' to finish): ")

        if need.lower() == "quit" or need == "":
            break

        cost = float(input("How much does it cost?: "))

        budget[need] = cost
        total_needs += cost

    savings = 0.20 * net_income
    wants = net_income - total_needs - savings

    print("\n----- Budget Summary -----")
    print("Income:", net_income)
    print("Needs:", total_needs)
    print("Savings:", savings)
    print("Money available to spend:", wants)

    return budget, wants, savings


calculate_budget()

print("\nNeeds Breakdown:")
print(budget)