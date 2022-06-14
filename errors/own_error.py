heigth=float(input("height: "))

weight = int((input("Weight: ")))

bmi = weight / heigth ** 2

if heigth > 3: 
    raise ValueError("Human Height should not be more then 3")

print(bmi)