# Student Grade Calculator Program

# This list will store results for all students
results = []

def calculate_grade(marks):
    """
    This function takes marks as input
    and returns the grade and teacher's comment.
    """
    if marks >= 90:
        return "A+", "Excellent performance!"
    elif marks >= 80:
        return "A", "Very good! Keep it up."
    elif marks >= 70:
        return "B", "Good work, but you can do even better."
    elif marks >= 60:
        return "C", "Satisfactory, try to improve."
    elif marks >= 50:
        return "D", "Needs improvement."
    else:
        return "F", "Fail — Work harder next time."

# Main program loop
while True:
    print("\n--- Student Grade Calculator ---")

    # Taking student name and marks
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks (0-100): "))

    # Get grade and comment using function
    grade, comment = calculate_grade(marks)

    # Store the result in a list as a dictionary
    results.append({
        "name": name,
        "marks": marks,
        "grade": grade,
        "comment": comment
    })

    # Print the result for the current student
    print(f"\nResult for {name}:")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Comment: {comment}")

    # Ask if user wants to continue
    choice = input("\nDo you want to enter another student? (yes/no): ")
    if choice.lower() != "yes":
        break

# Print final list of all student results
print("\n--- Final Results List ---")
for record in results:
    print(record)
