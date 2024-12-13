from data_store import employees

def add_performance_review():
    """Adds a performance review for an employee."""
    print("\n--- Add Performance Review ---")
    try:
        emp_id = int(input("Enter employee ID: "))
        if emp_id not in employees:
            print("Employee not found!")
            return

        review = input("Enter performance review: ")
        employees[emp_id]['performance_reviews'].append(review)
        print("Performance review added successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")

def view_performance_reviews():
    """Views all performance reviews for an employee."""
    print("\n--- View Performance Reviews ---")
    try:
        emp_id = int(input("Enter employee ID: "))
        if emp_id not in employees:
            print("Employee not found!")
            return

        reviews = employees[emp_id]['performance_reviews']
        if not reviews:
            print("No performance reviews for this employee.")
        else:
            print(f"Performance Reviews for {employees[emp_id]['name']}:")
            for idx, review in enumerate(reviews, start=1):
                print(f"{idx}. {review}")
    except ValueError:
        print("Invalid input. Please enter a valid numeric ID.")
