line = "=" * 36

print(line)
print('Project Phoenix')
print('Employee payroll processing system')
print(line)

employees = [
    {"id": "E101", "name": "Amit", "salary": 50000, "rating": 3},
    {"id": "E102", "name": "Neha", "salary": 70000, "rating": 5},
    {"id": "E103", "name": "Rahul", "salary": 90000, "rating": 4},
    {"id": "E104", "name": "Priya", "salary": 60000, "rating": 2},
    {"id": "E105", "name": "Karan", "salary": 80000, "rating": 5}
]

rating_criteria = [{"rating" : 1 , "bonus" : 0},
                   {"rating" : 2 , "bonus" : 0},
                   {"rating" : 3 , "bonus" : 5},
                   {"rating" : 4 , "bonus" : 10},
                   {"rating" : 5 , "bonus" : 15}]

processed_employees = []
cumulative_salary = 0
cumulative_bonus = 0
cumulative_final_salary = 0

def calculate_bonus_percentage(emp):
    rating = emp['rating']

    for r in rating_criteria:
        if r["rating"] == rating :
            bonus = r["bonus"]
            return bonus

    return 0

def calculate_bonus_amount(emp,bonus):
    bonus_amount = ( emp['salary'] * bonus ) / 100
    return bonus_amount

def calculate_final_salary(emp,bonus_amount):
    final_salary = emp['salary'] + bonus_amount
    return final_salary 

def process_employee(emp):
    emp_copy = emp.copy() # creating this so i dont end up touching original input employees DS
    process_bonus = calculate_bonus_percentage(emp_copy)
    emp_copy["bonus"] = process_bonus
    process_bonus_amount = calculate_bonus_amount(emp_copy,process_bonus)
    emp_copy["bonus_amount"] = process_bonus_amount
    process_final_salary = calculate_final_salary(emp_copy,process_bonus_amount)
    emp_copy["final_salary"] = process_final_salary
    #processed_employees.append(emp_copy)
    return emp_copy

for e in employees:
    final_record = process_employee(e)
    processed_employees.append(final_record)

for p in processed_employees:
    print(f"Employee ID: {p['id']}")
    print(f"Employee Name: {p['name']}")
    print(f"Original Salary: {p['salary']}")
    cumulative_salary += p['salary']
    print(f"Rating: {p['rating']}")
    print(f"Bonus Percentage: {p['bonus']}%")
    print(f"Bonus Amount: {p['bonus_amount']}")
    cumulative_bonus += p['bonus_amount']
    print(f"Final Salary: {p['final_salary']}")
    cumulative_final_salary += p['final_salary']
    print(line)

print(f'PAYROLL SUMMARY')
print(line)
print(f'Total employees processed: {len(processed_employees)}')
print(f'Total original payroll: {cumulative_salary}')
print(f'Total Bonus paid: {cumulative_bonus}')
print(f'Total Final payroll: {cumulative_final_salary}')



