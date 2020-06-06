credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
# print(credit_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

principal = int(input("Enter the credit principal:\n"))
calculation = input("""What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:     
""")

# months_count = 0
# monthly_payment = 0

if calculation == "m":
    months_count = int(input("Enter monthly payment:\n"))
elif calculation == "p":
    monthly_payment = int(input("Enter count of months:\n"))

if months_count % 10 == 1 or months_count != 11:
    m = 'month'
else:
    m = 'months'


payment = round(principal / months_count)
# last_payment = principal - (months_count - 1) * payment

print(f"It takes {payment} {m} to repay the credit")
print(f"Your monthly payment = {payment}")



