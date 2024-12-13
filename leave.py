from data_store import employees

def manage_leaves():
    """Updates leave details for an employee."""
    print("\n--- Manage Leaves ---")
    try:
        emp_id = int(input("Enter employee ID: "))
        if emp_id not in employees:
            print("Employee not found!")
            return

        leave_days = int(input("Enter number of leave days taken: "))
        employee = employees[emp_id]

        if leave_days > employee['leave_balance']:
            print("Insufficient leave balance!")
        else:
            employee['leaves_taken'] += leave_days
            employee['leave_balance'] -= leave_days
            print(f"Leave updated successfully for {employee['name']}.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
