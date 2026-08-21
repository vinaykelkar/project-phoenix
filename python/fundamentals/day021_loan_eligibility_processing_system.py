line = "=" * 36

print(line)
print('Project Phoenix')
print('Loan ELigibility Processing System')
print(line)

applicants = [
    {"id": "A101", "name": "Amit", "salary": 50000, "credit_score": 720, "existing_emi": 10000},
    {"id": "A102", "name": "Neha", "salary": 80000, "credit_score": 780, "existing_emi": 15000},
    {"id": "A103", "name": "Rahul", "salary": 40000, "credit_score": 650, "existing_emi": 5000},
    {"id": "A104", "name": "Priya", "salary": 100000, "credit_score": 810, "existing_emi": 30000},
    {"id": "A105", "name": "Karan", "salary": 60000, "credit_score": 690, "existing_emi": 12000}
]

loan_rules = {
    "minimum_salary": 45000,
    "minimum_credit_score": 700,
    "max_emi_percentage": 40
}

processed_applicants = []

def calculate_emi_percentage(existing_emi,salary):
    emi_percentage = (existing_emi / salary ) * 100
    return emi_percentage

def check_salary_eligibility(salary,min_salary):
    if salary >= min_salary:
        return True,"PASS"
    return False,"FAIL"

def check_credit_eligibility(credit_score,min_credit_score):
    if credit_score >= min_credit_score:
        return True, "PASS"
    return False,"FAIL"

def check_emi_eligibility(emi_percentage, max_emi_percentage):
    if emi_percentage <= max_emi_percentage:
        return True,"PASS"
    return False,"FAIL"

def process_applicant(applicant,loan_rule,pass_status="Eligible", fail_status="Not Eligible"):

    applicants_copy = applicant.copy()
    loan_rules_copy = loan_rule.copy()
    sal_eligible, sal_message = check_salary_eligibility(applicants_copy['salary'],loan_rules_copy['minimum_salary'])
    credit_eligible, credit_message = check_credit_eligibility(applicants_copy['credit_score'],loan_rules_copy['minimum_credit_score'])
    emi_pct = calculate_emi_percentage(applicants_copy['existing_emi'],applicants_copy['salary'])
    emi_eligible, emi_message = check_emi_eligibility(emi_pct,loan_rules_copy['max_emi_percentage'])

    applicants_copy["EMI_Percentage"] = emi_pct
    applicants_copy["salary_check"] = sal_message
    applicants_copy["credit_check"] = credit_message
    applicants_copy["EMI_check"] = emi_message

    if sal_eligible and credit_eligible and emi_eligible:
        applicants_copy["Final_status"] = pass_status
    else:
        applicants_copy["Final_status"] = fail_status

    return applicants_copy



if __name__ == "__main__":

    eligible_count = 0
    not_eligible_count = 0

    for a in applicants:
        processed_record = process_applicant(a,loan_rules)
        processed_applicants.append(processed_record)

    for p in processed_applicants:
        print(f"Applicant Id: {p['id']}")
        print(f"Name: {p['name']}")
        print(f"Salary: {p['salary']}")
        print(f"Credit score: {p['credit_score']}")
        print(f"Existing EMI: {p['existing_emi']}")
        print(f"EMI Percentage: {p['EMI_Percentage']}")
        print(f"")
        print(f"Salary Check: {p['salary_check']}")
        print(f"Credit Check: {p['credit_check']}")
        print(f"EMI Check: {p['EMI_check']}")
        print(f"")
        print(f"Final Status: {p['Final_status']}")
        if p['Final_status'] == "Eligible":
            eligible_count += 1
        else:
            not_eligible_count += 1

        print(line)

    print(f"LOAN ELIGIBILITY SUMMARY")
    print(line)

    print(f"Total applicants: {len(processed_applicants)}")
    print(f"Eligible applicants: {eligible_count}")
    print(f"Not eligible applicants: {not_eligible_count}")

