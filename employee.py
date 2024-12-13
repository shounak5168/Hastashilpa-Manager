# employee.py
from data_store import employees

def add_employee():
    """Adds a new employee."""
    print("\n--- Add Employee ---")
    try:
        name = input("Enter employee name: ")
        role = input("Enter employee role: ")
        salary = float(input("Enter employee salary: "))

        # Generate a unique employee ID based on existing entries
        emp_id = len(employees) + 1

        # Add the employee to the centralized employee dictionary
        employees[emp_id] = {
            'name': name,
            'role': role,
            'salary': salary,
            'leaves_taken': 0,
            'leave_balance': 30,
            'performance_reviews': []
        }

        print(f"Employee added successfully with ID: {emp_id}")
    except ValueError:
        print("Invalid input. Salary must be a number.")

def view_employees():
    """Displays all employees."""
    print("\n--- View Employees ---")
    if not employees:
        print("No employees to display.")
    else:
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Role: {details['role']}, Salary: {details['salary']}, Leaves Taken: {details['leaves_taken']}, Leave Balance: {details['leave_balance']}")
