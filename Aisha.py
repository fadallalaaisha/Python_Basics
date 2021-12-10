from typing import KeysView

def leapyear():
    years=range(1999,2021)
    for year in years:
        if year%4==0:print("{} is a leapyear".format(year))
    else:
        print("{} not a leapyear".format(year)) 

nun=range(50)
for x in nun:
    if x%2==0 & x%3==0:
        print("{} Fizzbuzz".format(x))
    else:
         x%2==0
         print("Fizz")

# add the sublist in one list    
a=[[1,2,4,5],[1,12,13,14],[10,20,30]]
b=[x for sublist in a for x in sublist]
print(b)
# timing the sublist by 10
x=[r*10 for r in a]
print(x)

y=[10,22,31,50]
# y.sort()
# print("laegest element:",y[0])
print("laegest element:",min(y))
# print(y[-1])

# odd numbers
odd=range(0,30)
for x in odd:
    if x%5==0:
        print('{} is odd number'.format(x))

sets={2,1,2,3,1,4,5,6,6,0}
print(sets)  
sets.remove(2)
print(sets)   
sets.update({10,20,30})
print(sets)

# list to set
list=[2,3,4,5,'a','s','c']
a=set(list)
print(a)

set1={11,12,13,14,15,2}
set2={11,2,15,'a','w','z','y'}
set3={1,2,3,'v','r','o'}

# set1.add(44)
# print(set1)
# set1.update([80,22,33,'ng'])
# print(set1)

m=set1.union(set2)
print(m)

k=set1.difference(set2)
print(k)

h=set1.intersection(set2)
print(h)

# Dictionary
places={"Nakuru":'you',"Kakuma":'she',"Nairobi":'me'}
# print(places)
print(places['Nairobi'])

countires={"Kenya":254,"Sudan":249,"Juba":211}
print(countires['Juba'])
a=countires.update({"Uganda":245,"Nairobi":100,"USA":191})
print(countires)
print(len(countires))
print('Kenya' in countires)

# how to access keys/values from the dictionary
d={"laptop":128,"Aisha":22,"phone":14000,"Sudan":211}
print(d.keys())
print(d.values())
# print(d[::-1])

