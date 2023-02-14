
li=[1,5,25,68,78,79,6,89,47,5,4,6, 69 , 64 ,54 ]

f=0
for item in li:
    if item == 47:
        f=1
    if f==0 and item%2==0:
        print("even",item)
    elif f==1 and item%2==1:
        print("odd",item)
