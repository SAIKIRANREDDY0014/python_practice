class Employee:

  def __init__(self,Empid,empname):
    self.Empid = Empid
    self.__empname = empname
  def getdet(self):
    return self.__empname
  def setdet(self,name):
    self.__empname = name
      

# e = Employee("3434","dsadf")
# # print(e.__empname)    
# print(e.getdet())

# e.setdet("sai kiran reddy")
# print(e.getdet())

class Student:
  def __init__(self,name,age):
    self.name = name 
    self._age = age
  

s1 = Student("sai",22)
print(s1._age)  