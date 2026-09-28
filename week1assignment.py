# Task 1: Get user's name and initialize total_spent
name = input("Enter your Name: ")
total_spent = 0

print("Hello, " + name + "! Let's track your spending for 3 days.")

# Task 2: Loop through 3 days
for day in range(1, 4):
    print("\nDay", day)
    spent = float(input("Enter money spent today ($): "))
    total_spent = total_spent + spent

    if spent > 20:
        print("Over your $20 budget today!")
    else:
        print("Great! Under budget today.")

# Task 3: Final Summary
print("\n----- Final Summary -----")
print("Total money spent over 3 days: $" + str(total_spent))

if total_spent <= 60:
    print("Overall Result: You stayed under your $60 total budget!")
else:
    print("Overall Result: You went over your $60 total budget!")