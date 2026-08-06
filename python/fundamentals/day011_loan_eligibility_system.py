line = "=" * 36

print(line)
print('Project Phoenix')
print('Loan Eligibility System')
print(line)

customer_name = input('Enter customer name: ').upper()
employment_type = input('Enter Customer employment type (SALARIED/SELF-EMPLOYED): ').upper()
monthly_income = float(input('Enter monthly income: '))
credit_score = int(input('Enter your credit score: '))
existing_monthly_emi = float(input('Enter Existing monthly EMI: '))

customer_profile = ['SALARIED','SELF-EMPLOYED']
credit_score_profiling = [{"min" : 300, "max" : 650, "status": "REJECTED"}, 
                          {"min" : 650, "max" : 750, "status": "REVIEW NEEDED"},
                          {"min" : 750, "max" : float('inf'), "status": "APPROVED"}]

maximum_emi_allowed = 0

print(f'Customer name: {customer_name}')

if existing_monthly_emi < 0 or monthly_income <= 0 or (credit_score < 300 or credit_score > 900) or employment_type not in customer_profile:
    print(f'Sorry, Loan application rejected!. For more detailed reason please reach out to the branch manager')

else:
    print(f'Employment type: {employment_type}')
    print(f'Monthly income: {monthly_income}')
    print(f'Existing EMI: {existing_monthly_emi}')

    if employment_type == "SALARIED":
        maximum_emi_allowed = monthly_income / 2
    else:
        maximum_emi_allowed = (monthly_income * 2 ) / 5

    print(f'Maximum EMI allowed: {maximum_emi_allowed}')
    print(f'Credit Score: {credit_score}')

    if existing_monthly_emi > maximum_emi_allowed:
        print(f"Sorry, your loan application was rejected because your current EMI is higher than the bank's maximum allowable limit.")
    else:

        for profile in credit_score_profiling:
            if profile['min'] <= credit_score < profile['max']:
                print(f"Loan status: {profile['status']}")




    

