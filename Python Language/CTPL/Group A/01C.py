''' 
If the marks obtained by a student in five different subjects are input through 
the keyboard, write a 
python 
program to calculate the aggregate marks and the 
percentage of marks obtained by the student. Assume that the maximum marks 
for each subject is 100. '''

a = int(input("Enter marks of subject 1: "))
b = int(input("Enter marks of subject 2: "))
c = int(input("Enter marks of subject 3: "))
d = int(input("Enter marks of subject 4: "))
e = int(input("Enter marks of subject 5: "))

agg = a+b+c+d+e
perc = agg/500*100

print(f"Aggregate: {agg}")
print(f"Percentage: {perc}")
