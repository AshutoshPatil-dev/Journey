n = str(input("Enter your name: "))
a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
agg = a+b
perc = agg/500*100
print("Name: {}".format(n)) #Old way of add a variable to print
print(f"Aggeregate: {agg}") # Using the f string new way, but it's only in 3.6+ and above I think...
print("Percentage: %.2f" % perc) #Using the C language way but with a confusing "%"?
print(f"Percentage: {perc:.2f}") #Using f string but with a floating and a decimal limit 