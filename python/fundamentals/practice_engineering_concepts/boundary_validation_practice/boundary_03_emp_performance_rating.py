
line = "=" * 36

print(line)
print('Practice Engineering Concepts')
print('Employee Performance classification')
print(line)


score_bracket = [{"min" : 0, "max" : 60, "rating" : "Poor", "min_inclusive" : True, "max_inclusive" : False},
               {"min" : 60, "max" : 75, "rating" : "Average", "min_inclusive" : True, "max_inclusive" : False},
               {"min" : 75, "max" : 90, "rating" : "Good", "min_inclusive" : True, "max_inclusive" : False},
               {"min" : 90, "max" : 100, "rating" : "Excellent", "min_inclusive" : True, "max_inclusive" : True}]


score = float(input('Please enter your score: '))

lower_end = False
upper_end = False

if score < 0 or score > 100:
    print(f'Incorrect score entered!')

else:

    for x in score_bracket:

        if x["min_inclusive"] == True:
            lower_end = score >= x["min"]
        else:
            lower_end = score > x["min"]

        if x["max_inclusive"] == False:
            upper_end = score < x["max"]
        else:
            upper_end = score <= x["max"]

        if lower_end and upper_end:
            print(f'Your scfore is {score} and hence rating is {x["rating"]}')
