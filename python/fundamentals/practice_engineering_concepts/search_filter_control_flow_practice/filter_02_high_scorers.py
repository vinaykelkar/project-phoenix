line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Filter high scorers')
print(line)

students = [
    {"id": "S101", "name": "Amit", "marks": 75},
    {"id": "S102", "name": "Neha", "marks": 88},
    {"id": "S103", "name": "Rahul", "marks": 62},
    {"id": "S104", "name": "Priya", "marks": 91}
]

condition_valid = False
minimum_marks = int(input('Please enter minimum marks : '))
matched_result = []

if minimum_marks < 0:
    print(f'Please enter correct marks greater than 0')

else:
    for s in students:
        if s['marks'] >= minimum_marks:
            condition_valid = True
            matched_result.append(s)
    

    if condition_valid == False:
        print(f'Students have less marks than what you entered')

    else:
        for x in matched_result:
            print(x)

    print(f'Total matched records : {len(matched_result)}')

