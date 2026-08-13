line = "=" * 36

print(line)
print('Project Phoenix')
print('Employee Directory Lookup System')
print(line)

employees = {
    "E101": {"name": "Amit", "department": "IT", "salary": 65000},
    "E102": {"name": "Neha", "department": "HR", "salary": 55000},
    "E103": {"name": "Rahul", "department": "FINANCE", "salary": 80000},
    "E104": {"name": "Priya", "department": "IT", "salary": 72000},
    "E105": {"name": "Karan", "department": "OPERATIONS", "salary": 60000}
}

emp_id = input('Please enter employee id : ').upper()
salary = 0

if emp_id not in employees:
    print(f'Employee not found')
else:
    print(f'Employee ID : {emp_id}')
    print(f'Name : {employees[emp_id]["name"]}')
    print(f'Department : {employees[emp_id]["department"]}')
    salary = employees[emp_id]["salary"]
    print(f'Salary : {salary}')
    if salary < 60000:
        print(f'Employee level : JUNIOR')
    elif 60000 <= salary < 75000:
        print(f'Employee level : MID LEVEL')
    else:
        print(f'Employee level : SENIOR')