line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Student lookup')
print(line)

students = [
    {"id": "S101", "name": "Amit", "marks": 75},
    {"id": "S102", "name": "Neha", "marks": 88},
    {"id": "S103", "name": "Rahul", "marks": 62},
    {"id": "S104", "name": "Priya", "marks": 91}
]

student_found = False
student_id = input('Please enter student id : ').upper()

for s in students:

    if s['id'] == student_id:
        student_found = True
        print(f"Name : {s['name']}")
        print(f"Name : {s['marks']}")
        break
    
if student_found == False:
    print(f'Student not found')
    
