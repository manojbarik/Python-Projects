# QUESTION:
# Create a Freelancer Management System using functions to:
# 1. Add clients and rates. 2. Log hours. 3. Show earnings. 4. Show summary.

# Global variables
rates = {}
hours = {}

def add():
    name = input("enter client name: ")
    price = float(input("enter hourly rate: "))
    rates[name] = price
    hours[name] = 0
    print("client added!")

def log():
    name = input("enter client name: ")
    if name in rates:
        work = float(input("enter hours: "))
        hours[name] += work
        print("hours logged!")
    else:
        print("not found!")

def show():
    name = input("enter client name: ")
    if name in rates:
        print(f"earnings: ${rates[name] * hours[name]}")
    else:
        print("not found!")

def summary():
    for name in rates:
        earn = rates[name] * hours[name]
        print(f"{name}: {hours[name]} hrs, ${earn}")

# Main loop
while True:
    print("\n1.Add 2.Log 3.Show 4.Summary 5.Exit")
    choice = input("choice: ")
    if choice == '1': add()
    elif choice == '2': log()
    elif choice == '3': show()
    elif choice == '4': summary()
    elif choice == '5': break
    else: print("invalid!")