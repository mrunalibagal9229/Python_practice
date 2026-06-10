days = int(input('enter days:'))
# // is floor division (integer division).
years = days //365
# % is the modulus operator.
days =days % 365

weeks = days //7
days = days % 7
print(f'YEARS:{years}\n WEEKS: {weeks}\n DAYS: {days}')

