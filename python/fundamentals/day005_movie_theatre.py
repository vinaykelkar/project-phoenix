line = "=" * 36

print(line)
print('Project Phoenix')
print('Movie Theatre')
print(line)

name = input('Enter your name: ')
age = int(input('Enter your age: '))

print(line)

if age < 1:
    print(f'Hello {name}')
    print('Baby less than an year old not allowed in theatre')
elif age < 5 and age >= 1:
    print(f'Hello {name}')
    print('Ticket Type: Free Ticket')
elif age >= 5 and age <= 17:
    print(f'Hello {name}')
    print('Ticket Type: Child Ticket')
elif age >= 18 and age <= 59:
    print(f'Hello {name}')
    print('Ticket Type: Adult Ticket')
else:
    print(f'Hello {name}')
    print('Ticket Type: Senior Citizen Ticket')
