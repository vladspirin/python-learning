import argparse
from math import ceil, log

parser = argparse.ArgumentParser(description="Credit Calculator Project")
parser.add_argument('--type', help="Type of Payment (Annuity or Differential")
parser.add_argument('--payment', help="Monthly payment", type=int)
parser.add_argument('--principal', help="Credit principal", type=int)
parser.add_argument('--periods', help="Count of months", type=int)
parser.add_argument('--interest', help="Credit interest (rate of interest)", type=float)

args = parser.parse_args()
if args.type not in ['annuity', 'diff']:
    print('Incorrect Parameters')
    exit(0)

if args.type == 'diff' and args.payment is not None:
    print('Incorrect Parameters')
    exit(0)

args_list = [args.type, args.payment, args.principal, args.periods, args.interest]

count = 0
for item in args_list:
    if item is None:
        count += 1

if count > 1:
    print('Incorrect Parameters')
    exit(0)

if args_list[1] is not None and args_list[1] < 0 or args_list[2] is not None and args_list[2] < 0 or \
        args_list[3] is not None and args_list[3] < 0 or args_list[4] is not None and args_list[4] < 0.0:
    print('Incorrect Ha ha')
    exit(0)

if args.type == 'annuity' and args.payment is not None and args.principal is not None and args.interest is not None:

    nominal_interest = args.interest / (12 * 100)

    months = ceil(log(args.payment
                      / (args.payment - nominal_interest * args.principal), (1 + nominal_interest)))

    overpayment = months * args.payment - args.principal

    year = months // 12
    months = months % 12

    if months == 0:
        print('You need', year, 'years to repay this credit!')
    elif year == 0:
        print('You need', months, 'months to repay this credit!')
    else:
        print('You need', year, 'years and', months, 'months to repay this credit!')
    print('Overpayment = ', overpayment)


elif args.type == 'annuity' and args.periods is not None and args.payment is not None and args.interest is not None:

    nominal_interest = args.interest / (12 * 100)

    complex_value = (nominal_interest * pow(1 + nominal_interest, args.periods)) / (
            pow(1 + nominal_interest, args.periods) - 1)
    credit_principal = int(args.payment / complex_value)

    overpayment = args.periods * args.payment - credit_principal

    print(f'Your credit principal = {credit_principal}!')
    print(f'Overpayment = {overpayment}')

elif args.type == 'annuity' and args.periods is not None and args.principal is not None and args.interest is not None:

    nominal_interest = args.interest / (12 * 100)

    complex_value = (nominal_interest * pow(1 + nominal_interest, args.periods)) / (
            pow(1 + nominal_interest, args.periods) - 1)

    monthly_payment = args.principal * complex_value
    overpayment = abs(args.periods * ceil(monthly_payment) - args.principal)
    monthly_payment = ceil(monthly_payment)
    print(f'Your annuity payment = {monthly_payment}!')

elif args.type == 'diff' and args.periods is not None and args.principal is not None and args.interest is not None:
    nominal_interest = args.interest / (12 * 100)
    diff_total_amount = 0
    for i in range(1, args.periods + 1):
        diff_amount = ceil(
            args.principal / args.periods + nominal_interest * args.principal * (1 - (i - 1) / args.periods))
        diff_total_amount += diff_amount
        print(f'Month {i}: paid out {diff_amount}')
    overpayment = diff_total_amount - args.principal
    print(f'Overpayment = {overpayment}')