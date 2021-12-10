#even
x=range(0,20)
for a in x:
    if a%2==0:
        print(a)

#odd
odd=range(30,50)
for o in odd:
    if o%5==0:
        print(o)

#empty list
y=range(100,200)
r=[]
for x in y:
    if x%7==0:
        r.append(x)        

def division():
    num=range(0,20)
    for n in num:
        if n%2==0:
            print("Fizz") 
        elif n%3==0:
            print("Buzz")  
        else:
            print("BuzzFizz")  
division()   

def evenNumbers():
    even=0
    while even < 50:
        even += 1
        if even%2==0:
            continue
        print(even)
evenNumbers()