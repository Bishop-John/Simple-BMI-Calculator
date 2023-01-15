print("Welcome to the B.M.I calculator")
weight_system = input("Press m to work in metric (cm/kg) or i to work in imperial (inches/lbs)")

if weight_system == "m":
    height = float(input("Please enter your height in metres: "))
    weight = float(input("Please enter your weight in kilograms: "))
    BMI = round((weight/height)/height,1)
elif weight_system == "i":
    height = float(input("Please enter your height in inches: "))
    weight = float(input("Please enter your weight in pounds: "))
    BMI = round((weight*703)/(height ** 2),1)
else:
    print ("An error has occured")
    exit

if BMI < 18.5:
    print ("You are classed as underweight")

elif 18.5 < BMI < 25:
    print ("You are classed as having a normal weight")

elif 25 < BMI < 30:
    print ("You are classed as overweight")

else:
    print ("You are classed as obese.")

