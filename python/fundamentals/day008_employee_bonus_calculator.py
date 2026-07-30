line = "=" * 36

print(line)
print('Project Phoenix')
print('Employee Bonus calculator')
print(line)

emp_name = input('Please enter your name: ')
emp_work_exp = float(input('Please enter your work experience: '))
emp_performance_rating = int(input('Please enter your performance rating (1-5): '))
emp_salary = int(input('Please enter your salary: '))

bonus_slab_1 = 5
bonus_slab_2 = 10
bonus_slab_3 = 15
work_bonus = 0

rating_bonus_1 = 5
rating_bonus_2 = 2
rating_bonus = 0 

final_salary = 0
final_bonus = 0
final_bonus_amount = 0

if emp_work_exp > 0 and emp_performance_rating >= 1 and emp_performance_rating <= 5 and emp_salary > 0:
    print(line)
    print(f'Employee Bonus summary')
    print(line)
    print(f'Employee Name: {emp_name}')
    print(f'Annual Salary: {emp_salary}')
    print(f'Years of Experience: {emp_work_exp}')
    print(f'Performance rating: {emp_performance_rating}')

    if emp_work_exp < 2:
        work_bonus = bonus_slab_1
        print(f'Base Bonus % is : {bonus_slab_1}')
    elif 2 <= emp_work_exp <= 5:
        work_bonus = bonus_slab_2
        print(f'Base Bonus % is : {bonus_slab_2}')
    else:
        work_bonus = bonus_slab_3
        print(f'Base Bonus % is : {bonus_slab_3}')
    
    if emp_performance_rating == 5:
        rating_bonus = rating_bonus_1
        print(f'Performance Bonus % is : {rating_bonus_1}')
    elif emp_performance_rating == 4:
        rating_bonus = rating_bonus_2
        print(f'Performance Bonus % is : {rating_bonus_2}')
    
    final_bonus = work_bonus + rating_bonus
    print(f'Total bonus % is : {final_bonus}')

    final_bonus_amount = (emp_salary * final_bonus ) / 100

    print(f'Total Bonus amount is : {final_bonus_amount}')

    final_salary = ( emp_salary + final_bonus_amount )
    print(f'Final salary : {final_salary}')


    
else:
    if emp_performance_rating < 1 or emp_performance_rating > 5:
        print(f'Incorrect rating entered')
    elif emp_work_exp <= 0:
        print(f'Either you entered incorrect work experience or you are a fresher and hence, you are not elgible for bonus')
    elif emp_salary <= 0:
        print(f'Salary cant be 0 or negative')