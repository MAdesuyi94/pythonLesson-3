salesperson_name = input("What is your name?: ")
years_with_company = int(input("How many years have you been with the company?: "))
base_salary = 2000
sales = int(input("How much money have you generated in sales?: "))
vacation_days = int(input("How many vacation days have you taken?: "))
if sales < 10000:
    commission_rate = 0
    rate_bonus = 0
elif sales > 10000 and sales < 100000:
    commission_rate = 0.02
    rate_bonus = 0
elif sales > 100000 and sales < 500000:
    commission_rate = 0.15
    rate_bonus = 1000
elif sales > 500000 and sales < 1000000:
    commission_rate = 0.28
    rate_bonus = 5000
else:
    commission_rate = 0.35
    rate_bonus = 100000

if years_with_company < 3:
    rate_bonus = 0

total_amount = base_salary + sales * commission_rate + rate_bonus

if years_with_company >= 5 and sales > 100000:
    additional_bonus = True
    total_amount += 1000
else:
    additional_bonus = False
if vacation_days > 3:
    pay_deducted = True
    total_amount -= 200
else:
    pay_deducted = False
print("==================================================================")
print(f"Name :                                 {salesperson_name}")
print(f"Longevity with company:                {years_with_company} years")
print(f"Base Salary:                           ${base_salary:,.2f}")
print(f"Commission Earned:                     ${sales * commission_rate:,.2f}")
print(f"Bonus Earned:                          ${rate_bonus:,.2f}")
if additional_bonus:
    print("Additional Longevity Bonus Earned:     $1000.00")
if pay_deducted:
    print("Pay Deducted for Excess Vacation Days: $200.00")
print("==================================================================")
print(f"Total Pay:                             ${total_amount:,.2f}")
print("==================================================================")
