# Define a function to determine the bonus rate based on the salary
def get_bonus_rate(salary):
    if salary >= 100000.00:
        return 0.20
    elif salary >= 50000.00:
        return 0.15
    else:
        return 0.10

# Open the file and read its content
def process_employee_data(file_name):
    total_bonus = 0  # To keep track of the total bonuses paid out

    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

            # Ensure the file has an even number of lines (name and salary pairs)
            if len(lines) % 2 != 0:
                print("Error: The file content is not in the correct format.")
                return

            for i in range(0, len(lines), 2):
                last_name = lines[i].strip()  # Remove leading/trailing whitespace from name
                salary = float(lines[i + 1].strip())  # Convert salary to a float

                # Get the bonus rate based on the salary
                bonus_rate = get_bonus_rate(salary)

                # Calculate the bonus
                bonus = salary * bonus_rate
                total_bonus += bonus

                # Display the employee's name, salary, and bonus
                print(f"Employee: {last_name}, Salary: ${salary:.2f}, Bonus: ${bonus:.2f}")

            # After the loop, print the total bonus
            print(f"\nTotal bonuses paid out: ${total_bonus:.2f}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except ValueError:
        print("Error: Invalid data format in the file.")


# Example usage:
# Create a sample file for testing
sample_file_name = "employee_data.txt"

# Sample data for testing (you can create your own file with similar structure)
with open(sample_file_name, 'w') as file:
    file.write("Adams\n50000.00\n")
    file.write("Baker\n75000.00\n")
    file.write("Smith\n45000.00\n")
    file.write("Jones\n105000.00\n")
    file.write("Taylor\n60000.00\n")

# Process the data from the file
process_employee_data(sample_file_name)
