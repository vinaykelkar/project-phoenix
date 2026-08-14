line = "=" * 36

print(line)
print('Project Phoenix')
print('Employee Directory Management System')
print(line)

employees = {
    "E101": {"name": "Amit", "department": "IT", "salary": 65000},
    "E102": {"name": "Neha", "department": "HR", "salary": 55000},
    "E103": {"name": "Rahul", "department": "FINANCE", "salary": 80000}
}

dept_list = ['IT','HR','FINANCE']
user_choices = ['ADD','UPDATE','DELETE']
operation_success = False

user_choice = input('Please enter the operation you want to perform (ADD/DELETE/UPDATE) : ').upper()

if user_choice in user_choices:
    emp_id = input(f'Enter employee id : ').upper()


    if user_choice == 'ADD':
        name = input(f'Enter employee name : ')
        dept = input(f'Enter department (IT/HR/FINANCE) : ').upper()
        salary = float(input('Enter salary : '))

        if emp_id in employees:
            print(f'ERROR : Employee already exists with employee id {emp_id}')
        elif dept not in dept_list:
            print(f'Invalid department {dept}')
        elif salary <= 0:
            print(f'Invalid salary entered {salary}')
        else:
            operation_success = True
            employees[emp_id] = {"name" : name, "department" : dept, "salary" : salary}
            print(f'Employee added : {employees[emp_id]}')

    elif user_choice == 'UPDATE':
        salary = float(input('Enter salary : '))
        if emp_id not in employees:
            print(f'ERROR : Employee does not exist with id {emp_id}')
        elif salary <= 0:
            print(f'Invalid salary entered {salary}')
        else:
            operation_success = True
            employees[emp_id]['salary'] = salary
            print(f'Employee updated : {employees[emp_id]}')

    elif user_choice == 'DELETE':
        if emp_id not in employees:
            print(f'ERROR : Employee does not exist with id {emp_id}')
        else:
            operation_success = True
            print(f'Employee deleted : {employees[emp_id]}')
            employees.pop(emp_id)


else:
    print(f'Incorrect usr choice entered {user_choice}')

if operation_success:
    print(employees)



