weight = float(input("Enter your weight : "))
unit = input("lbs or kg : ").lower() 
if unit == "lbs":
    final = weight/2.20
    print(f"Your weight is {final:.2f} kg")
elif unit == "kg":
    final = weight*2.20
    print(f"Your weight is {final:.2f} lbs")
else:
    print("Invalid weight unit")