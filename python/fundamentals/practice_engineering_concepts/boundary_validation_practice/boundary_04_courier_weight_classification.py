line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Courier Weight classification')
print(line)


weight_bracket = [{"min" : 0, "max" : 1, "charges" : 50, "min_inclusive" : True, "max_inclusive" : True},
               {"min" : 1, "max" : 5, "charges" : 120, "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 5, "max" : 10, "charges" : 250, "min_inclusive" : False, "max_inclusive" : True},
               {"min" : 10, "max" : float('inf'), "charges" : 500, "min_inclusive" : False, "max_inclusive" : True}]


weight = float(input('Please enter courier weight(KG): '))

lower_end = False
upper_end = False

if weight < 0 :
    print(f'Entered weight {weight} is incorrect')

else :

    for x in weight_bracket:
        if x["min_inclusive"] == True:
            lower_end = weight >= x["min"]
        else:
            lower_end = weight > x["min"]

        if x["max_inclusive"] == False:
            upper_end = weight < x["max"]
        else:
            upper_end = weight <= x["max"]

        if lower_end and upper_end:
            print(f'Entered weight {weight} is charged at {x["charges"]}')
