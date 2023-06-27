students = []

def take_student_entries():
    while True:
        name = input("Enter student name (or 'quit' to exit): ")
        if name.lower() == 'quit':
            break

        roll_no = input("Enter roll number: ")
        percentage = float(input("Enter percentage: "))
        year = int(input("Enter year: "))

        # Check if the roll number is already taken
        if any(student['roll_no'] == roll_no for student in students):
            print("Roll number already exists. Please enter a unique roll number.")
            continue

        student = {
            'name': name,
            'roll_no': roll_no,
            'percentage': percentage,
            'year': year
        }

        students.append(student)

    print_student_entries()

def print_student_entries():
    print("\nStudent Entries:")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Roll Number: {student['roll_no']}")
        print(f"Percentage: {student['percentage']}")
        print(f"Year: {student['year']}")
        print("-" * 20)

take_student_entries()