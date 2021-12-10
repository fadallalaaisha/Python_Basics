info=("kenya, 10022, Aisha")
print('location .address:',info)

def data():
    print("\nTwinkle, twinkle, little star,\n How I wonder what you are!\n Up above the world so high,\n Like a diamond in the sky. \n Twinkle, twinkle, little star,\n How I wonder what you are ")
data()

import sys,datetime
from typing import List, Tuple
print(sys.version)

# program to print current data and time
now=datetime.datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))

ME=("Narobi, 12233, Halima")
print("lacation address:",ME)

# program to print 1 and 2 name
def naming():
    frist_name="Aisha"
    last_name="Fadallala"
    print(frist_name + ' ' +last_name)
naming()    
# to accept first and last name
fname=input("Enter your first name:")
lname=input("Enter your last name:")
print("Hello your full name is:",fname+' '+lname)

# print the area of a cy
from math import pi
radius= float(input("Enter the radius"))
sum = radius ** 2 *pi
print("The total area is" ' ' + str(sum))

# Program to accept this (3, 5, 7, 23)
num = input("Type the provided numbers above:")
list = num.split(",")
tuple = tuple(list)
print("List:",list)
print('Tuple:',tuple)
