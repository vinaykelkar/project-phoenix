line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Insurance Premium classification')
print(line)


age_bracket = [{"min" : 0, "max" : 18, "premium" : "Not Eligible", "min_inclusive" : True, "max_inclusive" : False},
               {"min" : 18, "max" : 30, "premium" : 2000, "min_inclusive" : True, "max_inclusive" : True},
               {"min" : 30, "max" : 45, "premium" : 3500, "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 45, "max" : 60, "premium" : 5000, "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 60, "max" : float('inf'), "premium" : 8000, "min_inclusive" : False, "max_inclusive" : True}]


age = float(input('Please enter your age: '))

lower_end = False
upper_end = False
premium_amount = 0

#i can write < 18 not eleigible condition directly but want to handle via list of dicts only hence onlychecking negative age
if age < 0:
    print(f'Entered incorrect age {age} or not elgible for the policy as per company rules')

else :

    for x in age_bracket:

        if x["min_inclusive"] == True:
            lower_end = age >= x["min"]
        else:
            lower_end = age > x["min"]

        if x["max_inclusive"] == False:
            upper_end = age < x["max"]
        else:
            upper_end = age <= x["max"]

        if lower_end and upper_end:
            premium_amount = x["premium"]
            print(f'{premium_amount}')
