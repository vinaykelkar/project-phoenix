
line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Income Tax Slab classification')
print(line)


tax_bracket = [{"min" : 0, "max" : 3, "tax" : 0, "min_inclusive" : True, "max_inclusive" : True},
               {"min" : 3, "max" : 7, "tax" : 5, "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 7, "max" : 15, "tax" : 10, "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 15, "max" : float('inf'), "tax" : 20, "min_inclusive" : False, "max_inclusive" : True}]


income = float(input('Please enter your yearly income: '))

lower_end = False
upper_end = False

if income < 0:
    print(f'Incorrect income entered!')

else:

    for slab in tax_bracket:
        if slab["min_inclusive"] == True:
            lower_end = income >= slab["min"]
        else:
            lower_end = income > slab["min"]

        if slab["max_inclusive"] == False:
            upper_end = income < slab["max"]
        else:
            upper_end = income <= slab["max"]

        if lower_end and upper_end:
            print(f'Applicable tax rate for income {income} is {slab["tax"]}')
