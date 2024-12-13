from employee import add_employee, view_employees
from leave import manage_leaves
from salary import generate_salary_slip
from performance import add_performance_review, view_performance_reviews

def main():
    while True:
        print("\n--- Hastashilpa Manager ---")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Manage Leaves")
        print("4. Generate Salary Slip")
        print("5. Add Performance Review")
        print("6. View Performance Reviews")
        print("7. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Match the choice with the appropriate action
        try:
            if choice == "1":
                add_employee()  # Adds a new employee
            elif choice == "2":
                view_employees()  # Displays all employees
            elif choice == "3":
                manage_leaves()  # Updates leave details
            elif choice == "4":
                generate_salary_slip()  # Generates salary slip
            elif choice == "5":
                add_performance_review()  # Adds a performance review
            elif choice == "6":
                view_performance_reviews()  # Views performance reviews
            elif choice == "7":
                print("Exiting the system...")
                break  # Exit the loop
            else:
                print("Invalid choice! Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
