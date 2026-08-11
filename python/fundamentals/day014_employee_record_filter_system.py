line = "=" * 36

print(line)
print('Project Phoenix')
print('EMployee record filter system')
print(line)

employee_data = [{"id" : "E101", "Name" : "Amit", "Dept" : "IT", "Salary" : 65000, "Exp" : 4},
                 {"id" : "E102", "Name" : "Neha", "Dept" : "HR", "Salary" : 50000, "Exp" : 6},
                 {"id" : "E103", "Name" : "Rahul", "Dept" : "IT", "Salary" : 85000, "Exp" : 8},
                 {"id" : "E104", "Name" : "Priya", "Dept" : "FINANCE", "Salary" : 72000, "Exp" : 5},
                 {"id" : "E105", "Name" : "Karan", "Dept" : "IT", "Salary" : 45000, "Exp" : 2},
                 {"id" : "E106", "Name" : "Sneha", "Dept" : "FINANCE", "Salary" : 90000, "Exp" : 10},
                 {"id" : "E107", "Name" : "Arjun", "Dept" : "HR", "Salary" : 60000, "Exp" : 3},
                 {"id" : "E108", "Name" : "Meera", "Dept" : "IT", "Salary" : 78000, "Exp" : 7}]

department_name = input('Please enter department name (IT/HR/FINANCE): ').upper()
min_salary = float(input('Please enter minimum salary: '))
dept_list = ['HR','IT','FINANCE']

matched_result_employees = []


if min_salary <= 0 or department_name not in dept_list:
    print(f'Either salary {min_salary} you entered is less than equal to 0 or department name, {department_name}, you entered is invalid')
else:
    for x in employee_data:
        if department_name == x['Dept'] and min_salary <= x['Salary']:
            matched_result_employees.append(x)

    if len(matched_result_employees) == 0:
        print(f'No employees found matching the criteria, Department entered is {department_name} and salary entered is {min_salary} ')
    else:
        for y in matched_result_employees:
            print(f"Employee Id: {y['id']}")
            print(f"Employee Name: {y['Name']}")
            print(f"Employee Department: {y['Dept']}")
            print(f"Employee Salary: {y['Salary']}")
            print(f"Employee Experience: {y['Exp']}")
            print(line)

        print(f'Total employees found: {len(matched_result_employees)}')
        print(line)

