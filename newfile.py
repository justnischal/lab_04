# Define the employee data as a list of dictionaries
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

# Function to print the employee data
def print_employee_data(data):
    print("{:<12} {:<10} {:<4} {:<12}".format("Employee ID", "Name", "Age", "Salary (PM)"))
    for employee in data:
        print("{:<12} {:<10} {:<4} {:<12}".format(employee["Employee ID"], employee["Name"], employee["Age"], employee["Salary (PM)"]))

# Function to sort employee data based on the chosen parameter
def sort_employee_data(data, sort_param):
    if sort_param == 1:
        return sorted(data, key=lambda x: x["Age"])
    elif sort_param == 2:
        return sorted(data, key=lambda x: x["Name"])
    elif sort_param == 3:
        return sorted(data, key=lambda x: x["Salary (PM)"])
    else:
        return data

# Main program
print("Employee Data:")
print_employee_data(employee_data)

while True:
    try:
        sort_option = int(input("\nChoose sorting parameter (1. Age, 2. Name, 3. Salary, 0. Exit): "))
        if sort_option == 0:
            break
        if sort_option < 0 or sort_option > 3:
            print("Invalid option. Please enter a valid option.")
            continue

        sorted_data = sort_employee_data(employee_data, sort_option)
        print("\nSorted Employee Data:")
        print_employee_data(sorted_data)
    except ValueError:
        print("Invalid input. Please enter a valid option.")