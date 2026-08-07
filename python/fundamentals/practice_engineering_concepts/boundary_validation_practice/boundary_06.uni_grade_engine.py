line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('University Grade classification')
print(line)


grade_bracket = [{"min" : 0, "max" : 35, "grade" : "FAIL", "min_inclusive" : True, "max_inclusive" : False},
               {"min" : 35, "max" : 50, "grade" : "PASS", "min_inclusive" : True, "max_inclusive" : True},
               {"min" : 50, "max" : 60, "grade" : "SECOND CLASS", "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 60, "max" : 75, "grade" : "FIRST CLASS", "min_inclusive" : False, "max_inclusive" : False},
               {"min" : 75, "max" : 100, "grade" : "DISTINCTION", "min_inclusive" : True, "max_inclusive" : True}]


grade = float(input('Please enter your percentage (%): '))

lower_end = False
upper_end = False


if grade < 0 or grade > 100:
    print(f'Please enter correct grade percentage')

else :

    for x in grade_bracket:

        if x["min_inclusive"] == True:
            lower_end = grade >= x["min"]
        else:
            lower_end = grade > x["min"]

        if x["max_inclusive"] == False:
            upper_end = grade < x["max"]
        else:
            upper_end = grade <= x["max"]

        if lower_end and upper_end:
            print(f'Grade based on percentage {grade} is {x["grade"]}')