line = "=" * 36
print(line)
print('Project Phoenix')
print('Voting Eligibility Checker')
print(line)

name = input('Enter your name: ')
age = int(input('Enter your age: '))

print(f'Hello {name}!')

if age >= 18:
    print('You are eligible to vote')
else:
    print('You are NOT eligible to vote')