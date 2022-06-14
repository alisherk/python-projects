""" height = input("What is your height")

if height > 100:
    print("hello")
else:
    print("")
 """


""" num = input('your number ')

if int(num) % 2 != 0: 
    print('is odd')
else: 
    print('is even') """


""" 
h = float(input('what is your height '))

w = float(input('what is your weight '))

bmi =  round(w / h ** 2)

print(bmi)

if bmi < 18.5: 
    print('you are underweight')
elif bmi < 25: 
    print('You have normal weight')
elif bmi < 30: 200
    print('You are overweight')
else: 
    print('You are clinically obese')
  """


""" year = int(input('input year '))

if year % 4 == 0 and year % 100 == 0 and year % 500 == 0: 
    print(f'{year} is leap year')
else: 
    print('not leap year') """


h = int(input("what your age "))

bill = 0

if h >= 12:
    print("you can  ride")
    age = int(input("what is your age "))
    if age < 12:
        bill = 5
        print("Please pay $5")
    elif age <= 18:
        bill = 7
        print("Please pay $7")
    else:
        bill = 12
        print("Please pay $12")

    wants_photo = input("Do you want a photo? Y or No")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("you can't ride")
