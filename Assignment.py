# Function to calculate average and determine pass/fail
def calculate_average_and_status(marks):
    average = sum(marks) / len(marks)  # Calculate average
    status = "Pass" if average >= 40 else "Fail"  # Assuming passing mark is 40
    return average, status

# List to store student information
students = []

# Loop to get input for 3 students
for i in range(3):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter student name: ")
    marks = []
    for j in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {j}: "))
                if 0 <= mark <= 100:  # Ensure valid marks
                    marks.append(mark)
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    average, status = calculate_average_and_status(marks)
    students.append({
        "name": name,
        "marks": marks,
        "average": average,
        "status": status
    })

# Display results
print("\nStudent Results:")
for student in students:
    print(f"\nName: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Status: {student['status']}")
