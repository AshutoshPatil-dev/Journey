def noofchar():
    s = input("Enter a string: ")
    v = {}
    for i in s:
        v[i] = s.count(i)
    print(v)


print(len([i for i in input("Enter a string: ") if i.isdigit()]))

def dict_in_dict():
    f = {"child1": {"Name": "Anish", "Year": 2007},
        "child2": {"Name": "Ashu", "Year": 2007},
        "child3": {"Name": "Om", "Year": 2006}
        }
        
    for x,i in f.items():
        print(x)
        for y in i:
            print(y + ":",i[y])
            
pass
noofchar()
print()
digcount()
print()
dict_in_dict()
