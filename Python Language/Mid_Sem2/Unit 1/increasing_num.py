#This is better as a answer for this specific question
def pat1():
    n = 5
    for i in range(1,n+1):
        print("*"*i)
    print()
    
#This is better for logic building
def pat2():
    n = 5
    for i in range(1, n+1):
        for j in range(1,i+1):
            print("*", end='')
        print()

pat1()
pat2()