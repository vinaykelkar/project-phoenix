line = "=" * 36

print(line)
print(f'Project Phoenix')
print(f'Employee Salary Processing System')
print(line)

emp_name = input('Employee name: ').upper()
department = input('Department name (IT/HR/FINANCE):').upper()
basic_salary = float(input('Enter your salary: '))
years_of_service = float(input('Enter years of working in corporate setup: '))

hra = 0
bonus = 0
allowance = 0
gross_salary = 0
lower_match = False
upper_match = False

dept_list = ['HR','IT','FINANCE']

hra_rate = [{"min": 0, "max": 50000, "rate": 20},
       {"min": 50000, "max": float('inf'), "rate": 30}]

annual_bonus = [{"min": 0, "max": 2, "rate": 0, "min_inclusive": True, "max_inclusive" : False},
       {"min": 2, "max": 5, "rate": 10, "min_inclusive": True, "max_inclusive" : True},
       {"min": 5, "max": 40, "rate": 20, "min_inclusive": False, "max_inclusive" : False}]

dept_allowance = [{"dept": "IT", "rate" : 5000}, 
                  {"dept": "HR", "rate" : 3000}, 
                  {"dept": "FINANCE", "rate" : 4000}]

if basic_salary <= 0 or ( years_of_service < 0 or years_of_service >= 40) or department not in dept_list:
    # Assumption: corporate service is limited to 39 years.
    print(f'You are not eligible for salary processing please speak to HR')

else:
    print(f'Employee Name: {emp_name}')
    print(f'Department: {department}')
    print(f'Basic Salary: {basic_salary}')

    for x in hra_rate:
        if x['min'] <= basic_salary < x['max']:
            print(f"HRA %: {x['rate']}")  
            hra = ( basic_salary * x["rate"] ) / 100
            print(f'HRA amount: {hra}')
            break

    for y in annual_bonus:
        if y['min_inclusive'] == True:
            lower_match = years_of_service >= y['min']
        else:
            lower_match = years_of_service > y['min']

        if y['max_inclusive'] == False:
            upper_match = years_of_service < y['max']
        else:
            upper_match = years_of_service <= y['max']

        if lower_match and upper_match:

            print(f"Bonus %: {y['rate']}")
            bonus = ( basic_salary * y['rate'] ) / 100
            print(f'Bonus Amount: {bonus}')
            break

    for z in dept_allowance:
        if z['dept'] == department:
            allowance = z['rate']
            print(f'Allowance: {allowance}')
            break

    gross_salary = basic_salary + hra + bonus + allowance
    print(f'Gross salary: {gross_salary}')


    