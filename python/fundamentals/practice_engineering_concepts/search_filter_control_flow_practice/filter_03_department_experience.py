line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Department filter')
print(line)

employees = [
    {"id": "E101", "dept": "IT", "exp": 2},
    {"id": "E102", "dept": "HR", "exp": 6},
    {"id": "E103", "dept": "IT", "exp": 8},
    {"id": "E104", "dept": "FINANCE", "exp": 5},
    {"id": "E105", "dept": "IT", "exp": 4}
]

min_experience = float(input('Please enter minimum experience : '))
department = input('Pleae enter department name (IT/HR/FINANCE) : ').upper()
matched_result = []
condition_valid = False
dept_list = ['IT','HR','FINANCE']

if min_experience < 0 :
    print(f'Enter valid experience either 0 greater than 0')
elif department not in dept_list:
    print(f'Entered invalid department')

else:
    for e in employees:
        if e['dept'] == department and e['exp'] >= min_experience:
            condition_valid = True
            matched_result.append(e)

    if condition_valid == False:
        print(f'No match found')
    else:
        for x in matched_result:
            print(x)

    print(f'Total count : {len(matched_result)}')

    

         
