age = input('what is your age?')

age_int = int(age)

years = 90 - age_int 

days = years * 365

weeks = years * 52

months = years * 12 

print(f'You have {days} days, {weeks} weeks, {months} months')