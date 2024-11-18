Problem 5: Tuition Calculation Based on District Code
def tuition_calculation():
    with open('student_data.txt', 'r') as file:
        lines = file.readlines()

    total_tuition = 0
    student_count = 0

    print("\nName\tCredits\tTuition Owed")
    for i in range(0, len(lines), 3):
        name = lines[i].strip()
        district_code = lines[i + 1].strip()
        credits = int(lines[i + 2].strip())

        cost_per_credit = 250 if district_code == 'I' else 500
        tuition = credits * cost_per_credit
        total_tuition += tuition
        student_count += 1
        print(f"{name}\t{credits}\t${tuition:,.2f}")

    print(f"\nTotal tuition owed: ${total_tuition:,.2f}")
    print(f"Number of students: {student_count}")