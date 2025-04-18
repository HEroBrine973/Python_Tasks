# Step 1: Create a dictionary with student names and marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eva": 88
}

# Step 2: Ask user to input a student's name
name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display marks or show not found message
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print(f"No record found for student named '{name}'.")
