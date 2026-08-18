line = "=" * 36

print(line)
print('Project Phoenix')
print('Employee bonus calculator')
print(line)

employees = {
    "E101": {"name": "Amit", "salary": 50000, "experience": -1},
    "E102": {"name": "Neha", "salary": 70000, "experience": 5},
    "E103": {"name": "Rahul", "salary": 90000, "experience": 8},
    "E104": {"name": "Priya", "salary": 60000, "experience": 3}
}

employee_id = input('Enter employee id :').upper()

def validate(emp_id):
    if emp_id not in employees:
        return False
    return True

def calculate_bonus_percentage(emp_id):
    experience = employees[emp_id]["experience"]
    if 0 <= experience < 3:
        return 5
    elif 3 <= experience < 6:
        return 10
    else:
        return 15


def calculate_bonus_amount (salary,bonus_per):
    bonus = ( salary * bonus_per ) / 100
    return bonus

if validate(employee_id):
    employee_name = employees[employee_id]["name"]
    employee_salary = employees[employee_id]["salary"]
    employee_exp = employees[employee_id]["experience"]
    bonus_per = calculate_bonus_percentage(employee_id)
    final_bonus = calculate_bonus_amount(employee_salary,bonus_per)
    total_salary = employee_salary + final_bonus
    print(f'Employee id: {employee_id}')
    print(f'Employee name: {employee_name}')
    print(f'Salary : {employee_salary}')
    print(f'Experience: {employee_exp}')
    print(f'')
    print(f'Bonus Percentage: {bonus_per}%')
    print(f'Bonus amount: {final_bonus}')
    print(f'Total salary: {total_salary}')


else:
    print(f'Employee not found')
