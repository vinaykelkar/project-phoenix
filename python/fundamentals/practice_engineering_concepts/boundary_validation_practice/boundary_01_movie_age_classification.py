
line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Movie age classification')
print(line)

age_bracket = [{"min" : 0, "max" : 5, "category" : "Toddler", "min_inclusive" : True, "max_inclusive" : False},
               {"min" : 5, "max" : 12, "category" : "Child", "min_inclusive" : True, "max_inclusive" : True},
               {"min" : 12, "max" : 18, "category" : "Teen", "min_inclusive" : False, "max_inclusive" : False},
               {"min" : 18, "max" : float('inf'), "category" : "Adult", "min_inclusive" : True, "max_inclusive" : True}]

age = float(input('Please enter your age: '))

lower_end = False
upper_end = False

if age <= 0:
    print(f'The human life is not born yet!')

else:

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
            print(f'This age belongs to category: {x["category"]}')
