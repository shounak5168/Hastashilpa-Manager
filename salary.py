from data_store import employees

def generate_salary_slip():
    """Generates the salary slip for a given employee."""
    print("\n--- Generate Salary Slip ---")
    
    try:
        emp_id = int(input("Enter employee ID: "))
        
        # Check if the employee exists
        if emp_id not in employees:
            print("Employee not found!")
            return
        
        employee = employees[emp_id]
        
        # Basic salary (you can modify the logic for deductions, bonuses, etc.)
        basic_salary = employee['salary']
        
        # Sample deductions (can be modified according to requirements)
        pf_deduction = basic_salary * 0.12  # Example: 12% for PF
        other_deductions = 1000  # Example: Other deductions
        total_deductions = pf_deduction + other_deductions
        net_salary = basic_salary - total_deductions
        
        # Print salary slip
        print("\n--- Salary Slip ---")
        print(f"Employee ID: {emp_id}")
        print(f"Name: {employee['name']}")
        print(f"Role: {employee['role']}")
        print(f"Basic Salary: {basic_salary}")
        print(f"PF Deduction: {pf_deduction}")
        print(f"Other Deductions: {other_deductions}")
        print(f"Total Deductions: {total_deductions}")
        print(f"Net Salary: {net_salary}")
        
        # Including leave balance in the salary slip
        print(f"Leave Balance: {employee['leave_balance']}")

    except ValueError:
        print("Invalid input. Please enter a valid employee ID.")
