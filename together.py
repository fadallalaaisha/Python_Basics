
class Parent():
   def __init__(self,fname,fage):
       self.name=fname
       self.age=fage

       def results(self):
           print("self.name,self.age")

class Child(Parent):
    def __init__(self,fname,fage):
        Parent__init__(self,fname,fage,lastName)
        self.lastName="Tutu"

    def results(self):
        print('self.name,self.age,self.lastName')

ob=Child(20,'python')
ob.results
