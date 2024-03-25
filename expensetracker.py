import json
import os
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, description, category):
        today = datetime.now().strftime("%Y-%m-%d")
        self.expenses.append({"date": today, "amount": amount, "description": description, "category": category})

    def save_expenses(self, filename="expenses.json"):
        with open(filename, "w") as file:
            json.dump(self.expenses, file)

    def load_expenses(self, filename="expenses.json"):
        if os.path.exists(filename):
            with open(filename, "r") as file:
                self.expenses = json.load(file)

    def get_monthly_summary(self, month, year):
        monthly_expenses = [expense for expense in self.expenses if
                            datetime.strptime(expense["date"], "%Y-%m-%d").month == month and
                            datetime.strptime(expense["date"], "%Y-%m-%d").year == year]
        total_expenses = sum(expense["amount"] for expense in monthly_expenses)
        return total_expenses

    def get_category_summary(self, category):
        category_expenses = [expense["amount"] for expense in self.expenses if expense["category"] == category]
        total_expenses = sum(category_expenses)
        return total_expenses

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Summary")
        print("3. View Category-wise Summary")
        print("4. Save Expenses")
        print("5. Load Expenses")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the amount spent: "))
            description = input("Enter a brief description: ")
            category = input("Enter the category: ")
            tracker.add_expense(amount, description, category)
            print("Expense added successfully!")

        elif choice == "2":
            month = int(input("Enter the month (1-12): "))
            year = int(input("Enter the year: "))
            total_expenses = tracker.get_monthly_summary(month, year)
            print(f"Total expenses for {month}/{year}: ${total_expenses}")

        elif choice == "3":
            category = input("Enter the category: ")
            total_expenses = tracker.get_category_summary(category)
            print(f"Total expenses for {category}: ${total_expenses}")

        elif choice == "4":
            filename = input("Enter filename to save expenses (default is expenses.json): ")
            tracker.save_expenses(filename)
            print("Expenses saved successfully!")

        elif choice == "5":
            filename = input("Enter filename to load expenses from (default is expenses.json): ")
            tracker.load_expenses(filename)
            print("Expenses loaded successfully!")

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
