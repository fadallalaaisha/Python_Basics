class Employee:
    def __init__(self,first,last,country,pay):
        self.first=first
        self.last=last
        self.country=country
        self.pay=pay
        self.email=first + '.' + last  + '@company .com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last,self.country)       
    
    
emp_1=Employee( 'Aisha','Fadallala','Sudan',60000)
emp_2=Employee('Rouda','Bakira','Kenya',58880)

# print(emp_1)
# print(emp_2)

# emp_1.first='Aisha Fadallala'
# emp_1.last='Fadallala'
# emp_1.country='Sudan'
# emp_1.email='aisha@gmail.company.come'
# emp_1.pay=60000

# emp_2.name='Rouda'
# emp_1.last='Bakira'
# emp_2.country='Kenya'
# emp_2.email='roudamail.company.come'
# emp_2.pay=65000

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullName())




