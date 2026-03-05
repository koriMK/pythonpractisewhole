#string membership
#print ("Tiki" in "Tiki Joe")
it_rains = False

if it_rains:
    print("i will carry an umbrella ")

else:
    print("i will not carry an umbrella ")

"""
income tax calculator
gross income less than 1000 - tax = 5%
gross income less that 5000 and greater that or equal to 1000 -tax =10%
gross income less than 10000 and greater than or equal to 5000 -tax =15%
gross income greater than or equal to 10000 - tax = 20%

"""


gross_income = int(input("Enter your gross income"))

if gross_income < 1000:
    tax = gross_income * 0.05
elif gross_income >= 1000 and gross_income < 5000:
    tax = gross_income * 0.10
elif gross_income >= 5000 and gross_income < 10000:
    tax = gross_income * 0.15
else:
    tax = gross_income * 0.20 

net_income = gross_income - tax