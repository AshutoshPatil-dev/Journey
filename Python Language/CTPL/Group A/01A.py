'''Program to calculate the gross salary of an employee based on basic salary, dearness allowance, and house rent allowance. '''

bsal = float(input("Enter basic salary: "))

da = 0.5*bsal
hra = 0.2*bsal
gsal = bsal + da + hra

print(f"Gross Salary: {gsal}")
