
class Person ():
    def _init_(self,fname,lname):
      self.firstname=fname
      self.lastname=lname
      print('Person created')

class Student(Person):
   def _init_(self,fname,lname):
    Person._init_(self,fname,lname)
   print('Student Created')

 p1=Person('ali','yilmaz')
 s1=Student('çinar','solmaz')
 
  print(p1.firstname+' '+p1.lastname)
  print(s1.lastname+' '+s1.lastname)