weight=int(input("Enter your weight in kg: "))
height=float(input("Enter your height in metres: "))
bmi=weight/(height**2)
if bmi < 18.5:
   category="underweight"
elif 18.5 <= bmi < 25:
    category="normal"
elif 25 <= bmi < 30:
    category="overweight"
else:
    category="obesity"
print(f"Your bmi is {bmi:.2f} and you are {category}")
