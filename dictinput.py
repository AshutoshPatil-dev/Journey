'''s = input("Enter a string: ")
v = {}
for i in s:
    v[i] = s.count(i)
print(v)
'''
#No. of digits in a string
'''
count = [i for i in input("Enter a string: ") if i.isdigit()]
print(len(count))
'''

f = {"child1": {"Name": "Anish", "Year": 2007},
     "child2": {"Name": "Ashu", "Year": 2007},
     "child3": {"Name": "Om", "Year": 2006}
     }
for x,i in f.items():
    print(x)
    for y in i:
        print(y + ":",i[y])
