class employee:
 loc="GMU-SBP"
 def __init__(self,Empno,Ename,Sal):
  self.Empno=Empno
  self.Ename=Ename
  self.Sal=Sal
 def instancevariable(self):
  print("Employee No is",self.Empno)
  print("Employee No is",self.Ename)
  print("Employee No is",self.Sal)
  print("Employee No is",employee.loc)
emp1=employee(101,"PK Dixit",20000)
emp1.instancevariable()

emp2=employee(102,"Sam",80000)
emp2.instancevariable()